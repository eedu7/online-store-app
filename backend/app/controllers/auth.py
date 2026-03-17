from app.models import DBUser
from app.repositories import UserRepository
from app.schemas.requests.auth import UserLoginRequest, UserRegisterRequest
from app.schemas.responses.auth import AuthResponse
from app.schemas.responses.user import UserResponse
from core.controller import BaseController
from core.exceptions import DuplicateValueException, UnauthorizedException
from core.security import PasswordService
from core.security.jwt import JWTService


class AuthController(BaseController[DBUser]):
    def __init__(
        self,
        repository: UserRepository,
        jwt_service: JWTService,
        password_service: PasswordService,
    ) -> None:
        super().__init__(DBUser, repository)
        self.repository = repository
        self.jwt_service = jwt_service
        self.password_service = password_service

    async def register(self, payload: UserRegisterRequest) -> AuthResponse:

        if await self.repository.get_by_email(payload.email):
            raise DuplicateValueException(
                message="Email already registered",
                error_code="EMAIL_ALREADY_EXISTS",
                details={"email": payload.email},
            )

        if await self.repository.get_by_username(payload.username):
            raise DuplicateValueException(
                message="Username already registered",
                error_code="USERNAME_ALREADY_EXISTS",
                details={"username": payload.username},
            )

        hashed_password = self.password_service.hash_password(payload.password)

        user = await self.repository.create(
            {
                "email": payload.email,
                "username": payload.username,
                "password": hashed_password,
            }
        )
        await self.commit()

        token_pair = self.jwt_service.build_token_pair(
            str(user.id),
            extra_claims={"user": {"username": user.username, "email": user.email}},
        )

        return AuthResponse(token=token_pair, user=UserResponse.model_validate(user))

    async def login(self, payload: UserLoginRequest) -> AuthResponse:
        user = await self.repository.get_by_username_or_email(payload.username_or_email)

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

        return AuthResponse(token=token_pair, user=UserResponse.model_validate(user))
