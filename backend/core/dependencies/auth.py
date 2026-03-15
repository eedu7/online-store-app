from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.exceptions import UnauthorizedException
from core.security.jwt import JWTPayload, jwt_service


def auth_required(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None, Depends(HTTPBearer(auto_error=False))
    ],
) -> JWTPayload:
    if credentials is None:
        raise UnauthorizedException(
            message="Authorization header missing", error_code="MISSING_AUTH_HEADER"
        )

    return jwt_service.decode_token(credentials.credentials, expected_token="access")


AuthenticationRequired = Annotated[JWTPayload, Depends(auth_required)]
