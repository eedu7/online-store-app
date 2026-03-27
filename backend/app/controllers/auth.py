from datetime import timedelta

from fastapi import Request, Response

from app.models import DBRole, DBUser
from app.repositories import RoleRepository, UserRepository, UserRoleRepository
from app.schemas.requests.auth import (
    UserLoginRequest,
    UserLogoutRequest,
    UserRegisterRequest,
)
from app.schemas.responses.auth import AuthResponse
from app.schemas.responses.user import UserResponse
from core.config import config
from core.controller import BaseController
from core.exceptions import (
    BadRequestException,
    DuplicateValueException,
    InternalServerException,
    UnauthorizedException,
)
from core.security import PasswordService
from core.security.jwt import JWTService


class AuthController(BaseController[DBUser]):
    def __init__(
        self,
        user_repository: UserRepository,
        role_repository: RoleRepository,
        user_role_repository: UserRoleRepository,
        jwt_service: JWTService,
        password_service: PasswordService,
    ) -> None:
        super().__init__(DBUser, user_repository)
        self.user_repository = user_repository
        self.role_repository = role_repository
        self.user_role_repository = user_role_repository
        self.jwt_service = jwt_service
        self.password_service = password_service

    async def register(
        self, payload: UserRegisterRequest, response: Response
    ) -> AuthResponse:

        if await self.user_repository.get_by_email(payload.email):
            raise DuplicateValueException(
                message="Email already registered",
                error_code="EMAIL_ALREADY_EXISTS",
                details={"email": payload.email},
            )

        if await self.user_repository.get_by_username(payload.username):
            raise DuplicateValueException(
                message="Username already registered",
                error_code="USERNAME_ALREADY_EXISTS",
                details={"username": payload.username},
            )

        hashed_password = self.password_service.hash_password(payload.password)

        user = await self.user_repository.create(
            {
                "email": payload.email,
                "username": payload.username,
                "password": hashed_password,
            }
        )
        await self.flush()

        role = await self._get_or_create_customer_role()

        await self._assign_role(user, role)

        await self.commit()
        await self.refresh(user)

        token_pair = self.jwt_service.build_token_pair(
            str(user.id),
            extra_claims={"user": {"username": user.username, "email": user.email}},
        )

        auth_response = AuthResponse(
            token=token_pair, user=UserResponse.model_validate(user)
        )
        self._set_cookies(auth_response, response)
        return auth_response

    async def login(
        self, payload: UserLoginRequest, response: Response
    ) -> AuthResponse:
        user = await self.user_repository.get_by_username_or_email(
            payload.username_or_email
        )

        if user is None:
            raise UnauthorizedException(
                message="Invalid credentials", error_code="INVALID_CREDENTIALS"
            )

        if user.password and not self.password_service.verify_password(
            user.password, payload.password
        ):
            raise UnauthorizedException(
                message="Invalid credentials", error_code="INVALID_CREDENTIALS"
            )

        token_pair = self.jwt_service.build_token_pair(
            str(user.id),
            extra_claims={"user": {"username": user.username, "email": user.email}},
        )

        auth_response = AuthResponse(
            token=token_pair, user=UserResponse.model_validate(user)
        )
        self._set_cookies(auth_response, response)
        return auth_response

    async def logout(self, payload: UserLogoutRequest, request: Request) -> None:
        print("STEP 01")
        if payload.access_token is None:
            print("STEP 02")
            payload.access_token = request.cookies.get("ACCESS_TOKEN")
        if payload.refresh_token is None:
            print("STEP 03")
            payload.refresh_token = request.cookies.get("REFRESH_TOKEN")

        print("STEP 04")
        if not payload.model_dump(exclude_none=True):
            print("STEP 05")
            raise BadRequestException("No credentials provided")

        print("STEP 06")
        await self.jwt_service.revoke_tokens(**payload.model_dump(exclude_none=True))
        print("STEP 07")
        self._delete_cookies(request)

    def _set_cookies(self, payload: AuthResponse, response: Response) -> None:
        is_secure = config.COOKIE_SECURE
        samesite = config.COOKIE_SAMESITE

        response.set_cookie(
            key="ACCESS_TOKEN",
            value=payload.token.access_token,
            max_age=int(
                timedelta(
                    minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
                ).total_seconds()
            ),
            httponly=True,
            secure=is_secure,
            samesite=samesite,
        )
        response.set_cookie(
            key="REFRESH_TOKEN",
            value=payload.token.refresh_token,
            max_age=int(
                timedelta(days=config.JWT_REFRESH_TOKEN_EXPIRE_DAYS).total_seconds()
            ),
            httponly=True,
            secure=is_secure,
            samesite=samesite,
        )

    def _delete_cookies(self, request: Request) -> None:
        request.cookies.clear()

    async def _get_or_create_customer_role(self) -> DBRole:
        try:
            existing_role = await self.role_repository.get_one_by_filters(
                {"name": "customer"}
            )
            if existing_role:
                return existing_role

            # create new role
            new_role = await self.role_repository.create(
                {"name": "customer", "description": "A customer"}
            )

            await self.flush()
            return new_role
        except Exception:
            raise InternalServerException("Failed to initialize customer role")

    async def _assign_role(self, user: DBUser, role: DBRole) -> None:
        try:
            await self.user_role_repository.create(
                {"user_id": user.id, "role_id": role.id}
            )

        except Exception:
            raise InternalServerException(f"Failed to assign {role.name} role to user")
