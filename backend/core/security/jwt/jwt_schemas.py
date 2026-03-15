from datetime import datetime
from typing import Any, Dict, Literal

from pydantic import BaseModel, Field

JWTType = Literal["access", "refresh"]


class JWTPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # access token TTL in seconds


class JWTPayload(BaseModel):
    sub: str
    type: JWTType
    jti: str
    iat: datetime
    exp: datetime
    nbf: datetime | None = None
    iss: str | None = None
    aud: str | None = None
    extra: Dict[str, Any] = Field(default_factory=dict)
