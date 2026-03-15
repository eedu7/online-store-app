from app.models import DBUser
from app.repositories import UserRepository
from app.schemas.requests.auth import UserLoginRequest, UserRegisterRequest
from core.controller import BaseController
from core.exceptions import DuplicateValueException, UnauthorizedException
from core.security import password_service
from core.security.jwt import jwt_service


class AuthController(BaseController[DBUser]):
    def __init__(self, repository: UserRepository) -> None:
        super().__init__(DBUser, repository)
        self.repository = repository

    async def register(self, payload: UserRegisterRequest) -> DBUser:

        if self.repository.get_by_email(payload.email):
            raise DuplicateValueException(
                message="Email already registered",
                error_code="EMAIL_ALREADY_EXISTS",
                details={"email": payload.email},
            )

        if self.repository.get_by_username(payload.username):
            raise DuplicateValueException(
                message="Username already registered",
                error_code="USERNAME_ALREADY_EXISTS",
                details={"username": payload.username},
            )

        hashed_password = password_service.hash_password(payload.password)

        user = await self.repository.create(
            {
                "email": payload.email,
                "username": payload.username,
                "password": hashed_password,
            }
        )
        await self.commit()
        return user

    async def login(self, payload: UserLoginRequest):
        user = await self.repository.get_by_username_or_email(payload.username_or_email)

        if user is None:
            raise UnauthorizedException(
                message="Invalid credentials", error_code="INVALID_CREDENTIALS"
            )

        if user.password and not password_service.verify_password(
            user.password, payload.password
        ):
            raise UnauthorizedException(
                message="Invalid credentials", error_code="INVALID_CREDENTIALS"
            )

        return jwt_service.build_token_pair(
            str(user.id), extra_claims={"username": user.username, "email": user.email}
        )
