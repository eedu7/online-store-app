from typing import Annotated

from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.exceptions import UnauthorizedException
from core.security.jwt import JWTPayload, JWTServiceDep


async def auth_required(
    request: Request,
    credentials: Annotated[
        HTTPAuthorizationCredentials | None, Depends(HTTPBearer(auto_error=False))
    ],
    jwt_service: JWTServiceDep,
) -> JWTPayload:
    print("Cookies:", request.cookies)
    token = None
    print("Step 01")
    if credentials:
        print("Step 02")
        token = credentials.credentials
    else:
        print("Step 03")
        cookie_token = request.cookies.get("ACCESS_TOKEN")
        if cookie_token:
            print("Step 04")
            token = cookie_token
        else:
            print("Step 05")
            raise UnauthorizedException(
                message="Authorization header is missing",
                error_code="AUTH_HEADER_MISSING",
            )
    print("Token:", token)

    payload = jwt_service.decode_token(token, expected_token="access")

    revoked = await jwt_service.is_token_revoked(payload.jti)

    if revoked:
        raise UnauthorizedException(
            message="Token has been revoked", error_code="AUTH_TOKEN_REVOKED"
        )

    return payload


AuthenticationRequired = Annotated[JWTPayload, Depends(auth_required)]
