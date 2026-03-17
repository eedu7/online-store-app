from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.exceptions import UnauthorizedException
from core.security.jwt import JWTPayload, JWTServiceDep


async def auth_required(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None, Depends(HTTPBearer(auto_error=False))
    ],
    jwt_service: JWTServiceDep,
) -> JWTPayload:
    if credentials is None:
        raise UnauthorizedException(
            message="Authorization header is missing", error_code="AUTH_HEADER_MISSING"
        )

    payload = jwt_service.decode_token(credentials.credentials, expected_token="access")

    revoked = await jwt_service.is_token_revoked(payload.jti)

    if revoked:
        raise UnauthorizedException(
            message="Token has been revoked", error_code="AUTH_TOKEN_REVOKED"
        )

    return payload


AuthenticationRequired = Annotated[JWTPayload, Depends(auth_required)]
