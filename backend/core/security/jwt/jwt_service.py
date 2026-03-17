from datetime import datetime, timedelta, timezone
from typing import Annotated, Any, Dict
from uuid import uuid4

import jwt
from fastapi import Depends
from jwt.exceptions import (
    DecodeError,
    ExpiredSignatureError,
    ImmatureSignatureError,
    InvalidAlgorithmError,
    InvalidAudienceError,
    InvalidIssuerError,
    InvalidSignatureError,
    MissingRequiredClaimError,
)

from core.config import config
from core.exceptions import InternalServerException
from core.redis.stores import TokenRevocationStore, TokenRevocationStoreDep
from core.security.jwt.jwt_exceptions import (
    InvalidTokenException,
    InvalidTokenTypeException,
    MissingTokenException,
    TokenExpiredException,
)
from core.security.jwt.jwt_schemas import JWTPair, JWTPayload, JWTType


class JWTService:
    def __init__(self, revocation_store: TokenRevocationStore) -> None:
        self._revocation_store = revocation_store

    def build_token_pair(
        self,
        subject: str,
        extra_claims: Dict[str, Any] | None = None,
    ) -> JWTPair:
        access_ttl = timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_ttl = timedelta(days=config.JWT_REFRESH_TOKEN_EXPIRE_DAYS)

        claims = extra_claims or {}

        access_token = self._build_token(
            subject,
            "access",
            ttl=access_ttl,
            extra_claims=claims,
        )
        refresh_token = self._build_token(
            subject,
            "refresh",
            ttl=refresh_ttl,
            extra_claims=claims,
        )

        return JWTPair(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=int(access_ttl.total_seconds()),
        )

    def decode_token(
        self,
        token: str | None,
        *,
        expected_token: JWTType | None = None,
        verify_exp: bool = True,
    ) -> JWTPayload:
        if not token or not token.strip():
            # raise MissingTokenException
            raise MissingTokenException()

        raw_payload = self._decode_jwt(token=token, verify_exp=verify_exp)
        payload = self._build_payload(raw_payload)

        # TODO: Revocation check (must happen after successful decode)

        if expected_token is not None and payload.type != expected_token:
            raise InvalidTokenTypeException(
                expected=expected_token, received=payload.type
            )

        return payload

    def refresh_access_token(
        self, refresh_token: str, extra_claims: Dict[str, Any] | None = None
    ) -> JWTPair:
        payload = self.decode_token(refresh_token, expected_token="refresh")
        # TODO: Rotate; Revoke the consumed refresh token immediately
        # self.revoke_token(payload.jti)

        return self.build_token_pair(
            subject=payload.sub, extra_claims={**payload.extra, **(extra_claims or {})}
        )

    def revoke_token(self, jti: str) -> None:
        # TODO: Revoke Token
        raise NotImplementedError("revoke_token: wire up a Redis/DB revocation store")

    def revoke_token_by_raw(self, token: str) -> None:
        payload = self.decode_token(token, verify_exp=False)
        self.revoke_token(payload.jti)

    def is_token_revoked(self, jti: str) -> bool:
        # TODO: Check revocation store (Redis/DB)
        raise NotImplementedError(
            "is_token_revoked: wire upa Redis/DB revocation store"
        )

    def decode_expired_token(self, token: str) -> JWTPayload:
        return self.decode_token(token, verify_exp=False)

    def _build_token(
        self,
        subject: str,
        token_type: JWTType,
        ttl: timedelta,
        extra_claims: Dict[str, Any],
    ) -> str:
        now = datetime.now(tz=timezone.utc)

        payload: Dict[str, Any] = {
            "sub": subject,
            "type": token_type,
            "jti": str(uuid4()),
            "iat": now,
            "nbf": now,
            "exp": now + ttl,
            **extra_claims,
        }

        if config.JWT_ISSUER:
            payload["iss"] = config.JWT_ISSUER
        if config.JWT_AUDIENCE:
            payload["aud"] = config.JWT_AUDIENCE

        try:
            return jwt.encode(
                payload, key=config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM
            )
        except Exception as exc:
            raise InternalServerException(
                message="Token creation failed", details={"reason": str(exc)}
            ) from exc

    def _decode_jwt(self, token: str, *, verify_exp: bool) -> Dict[str, Any]:
        options: Dict[str, Any] = {
            "verify_exp": verify_exp,
            "verify_nbf": True,
            "verify_iss": bool(config.JWT_ISSUER),
            "verify_aud": bool(config.JWT_AUDIENCE),
            "require": ["sub", "jti", "iat", "exp", "type"],
        }

        decode_kwargs: Dict[str, Any] = {
            "algorithms": [config.JWT_ALGORITHM],
            "options": options,
            "leeway": timedelta(seconds=config.JWT_LEEWAY_SECONDS),
        }
        if config.JWT_ISSUER:
            decode_kwargs["issuer"] = config.JWT_ISSUER
        if config.JWT_AUDIENCE:
            decode_kwargs["audience"] = config.JWT_AUDIENCE

        try:
            return jwt.decode(token, key=config.JWT_SECRET_KEY, **decode_kwargs)
        except ExpiredSignatureError as exc:
            raise TokenExpiredException() from exc
        except InvalidSignatureError as exc:
            raise InvalidTokenException(
                message="Token signature verification failed"
            ) from exc
        except (InvalidIssuerError, InvalidAudienceError) as exc:
            raise InvalidTokenException(message=str(exc)) from exc
        except MissingRequiredClaimError as exc:
            raise InvalidTokenException(
                message=f"Token is missing required claim: {exc.claim}"
            ) from exc
        except InvalidAlgorithmError as exc:
            raise InvalidTokenException(
                message=f"Token uses an unsupported algorithm: {exc}"
            ) from exc
        except DecodeError as exc:
            raise InvalidTokenException(
                message="Token could not be decoded - it may be malformed"
            ) from exc
        except ImmatureSignatureError as exc:
            raise InvalidTokenException(
                message="Token is not yet valid (nbf claim)"
            ) from exc
        except Exception as exc:
            raise InternalServerException(
                message="Token validation encountered an unexpected error",
                details={"reason": str(exc)},
            ) from exc

    def _build_payload(self, raw: Dict[str, Any]) -> JWTPayload:
        known_keys = {"sub", "type", "jti", "iat", "exp", "nbf", "iss", "aud"}

        try:
            return JWTPayload(
                sub=raw["sub"],
                type=raw["type"],
                jti=raw["jti"],
                iat=datetime.fromtimestamp(raw["iat"], tz=timezone.utc),
                exp=datetime.fromtimestamp(raw["exp"], tz=timezone.utc),
                nbf=(
                    datetime.fromtimestamp(raw["nbf"], tz=timezone.utc)
                    if "nbf" in raw
                    else None
                ),
                iss=raw.get("iss"),
                aud=raw.get("aud"),
                extra={
                    key: value for key, value in raw.items() if key not in known_keys
                },
            )
        except (KeyError, ValueError) as exc:
            raise InvalidTokenException(
                message=f"Token payload is malformed: {exc}"
            ) from exc


def get_jwt_service(revocation_store: TokenRevocationStoreDep) -> JWTService:
    return JWTService(revocation_store)


JWTServiceDep = Annotated[JWTService, Depends(get_jwt_service)]
