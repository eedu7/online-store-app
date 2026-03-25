from datetime import timedelta

from fastapi import Request, Response

from app.models import DBUser
from app.repositories import UserRepository
from app.schemas.requests.auth import (
    UserLoginRequest,
    UserLogoutRequest,
    UserRegisterRequest,
)
from app.schemas.responses.auth import AuthResponse
from app.schemas.responses.user import UserResponse
from core.config import config
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

    async def register(
        self, payload: UserRegisterRequest, response: Response
    ) -> AuthResponse:

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

        auth_response = AuthResponse(
            token=token_pair, user=UserResponse.model_validate(user)
        )
        self._set_cookies(auth_response, response)
        return auth_response

    async def login(
        self, payload: UserLoginRequest, response: Response
    ) -> AuthResponse:
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

        auth_response = AuthResponse(
            token=token_pair, user=UserResponse.model_validate(user)
        )
        self._set_cookies(auth_response, response)
        return auth_response

    async def logout(self, payload: UserLogoutRequest, request: Request) -> None:
        self._delete_cookies(request)
        await self.jwt_service.revoke_tokens(**payload.model_dump())

    def _set_cookies(self, payload: AuthResponse, response: Response) -> None:
        is_secure = config.COOKIE_SECURE
        samesite = config.COOKIE_SAMESITE
        domain = config.COOKIE_DOMAIN

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
            domain=domain,
            path="/",
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
            domain=domain,
            path="/",
        )

    def _delete_cookies(self, request: Request) -> None:
        request.cookies.clear()
