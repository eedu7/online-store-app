import secrets

from app.models import DBRole, DBUser
from app.repositories import RoleRepository, UserRepository, UserRoleRepository
from app.schemas.requests.boostrap import SuperuserInRequest
from app.schemas.responses.auth import AuthResponse
from app.schemas.responses.user import UserResponse
from core.config import config
from core.controller import BaseController
from core.exceptions import (
    BadRequestException,
    InternalServerException,
    UnauthorizedException,
)
from core.security import PasswordService
from core.security.jwt import JWTService


class SuperuserBootstrap(BaseController[DBUser]):
    def __init__(
        self,
        user_repository: UserRepository,
        user_role_repository: UserRoleRepository,
        role_repository: RoleRepository,
        jwt_service: JWTService,
        password_service: PasswordService,
    ) -> None:
        super().__init__(DBUser, user_repository)
        self.user_repository = user_repository
        self.user_role_repository = user_role_repository
        self.role_repository = role_repository
        self.jwt_service = jwt_service
        self.password_service = password_service

    async def create_superuser(
        self, payload: SuperuserInRequest, secret: str
    ) -> AuthResponse:
        try:
            # Verify the bootstrap secret
            await self._verify_bootstrap_secret(secret)

            # Get or create superuser role
            super_user_role = await self._get_or_create_super_user_role()

            # Create the superuser
            super_user_account = await self._create_superuser_account(payload)

            # Assigning the role
            await self._assign_role(super_user_account, super_user_role)

            # Commit all changes
            await self.commit()
            await self.refresh(super_user_account)

            token_pair = self.jwt_service.build_token_pair(
                str(super_user_account.id),
                extra_claims={
                    "user": {
                        "username": super_user_account.username,
                        "email": super_user_account.email,
                    }
                },
            )

            return AuthResponse(
                token=token_pair, user=UserResponse.model_validate(super_user_account)
            )

        except (UnauthorizedException, BadRequestException):
            await self.rollback()
            raise
        except Exception:
            await self.rollback()
            raise InternalServerException(
                "Failed to create superuser. Please try again"
            )

    async def _verify_bootstrap_secret(self, provided_secret: str) -> None:
        if not secrets.compare_digest(
            provided_secret.encode(), config.BOOTSTRAP_SECRET.encode()
        ):
            raise UnauthorizedException("Invalid credentials")

    async def _get_or_create_super_user_role(self) -> DBRole:
        try:
            existing_role = await self.role_repository.get_one_by_filters(
                {"name": "super_user"}
            )
            if existing_role:
                return existing_role

            # Create new superuser role
            super_user_role = await self.role_repository.create(
                {"name": "super_user", "description": "SuperUser"}
            )

            await self.flush()
            return super_user_role
        except Exception:
            raise InternalServerException("Failed to initialize 'super user' role")

    async def _create_superuser_account(self, payload: SuperuserInRequest) -> DBUser:
        try:
            existing_users = await self.user_repository.get_all(limit=1)
            if len(existing_users) > 0:
                raise BadRequestException(
                    "System already initialized. Superuser creation is only allowed once."
                )

            # Hash the password
            hashed_password = self.password_service.hash_password(payload.password)

            # Create the superuser account
            super_user_account = await self.user_repository.create(
                {
                    "username": payload.username,
                    "email": payload.email,
                    "password": hashed_password,
                    "email_verified": True,
                    "first_name": payload.first_name,
                    "last_name": payload.last_name,
                }
            )
            await self.flush()

            return super_user_account

        except BadRequestException:
            raise
        except Exception:
            raise InternalServerException("Failed to create superuser account")

    async def _assign_role(self, user: DBUser, role: DBRole) -> None:
        try:
            await self.user_role_repository.create(
                {"user_id": user.id, "role_id": role.id}
            )

        except Exception:
            raise InternalServerException(f"Failed to assign {role.name} role to user")
