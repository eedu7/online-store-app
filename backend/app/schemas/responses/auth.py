from pydantic import BaseModel

from app.schemas.responses.user import UserResponse
from core.security.jwt import JWTPair


class AuthResponse(BaseModel):
    token: JWTPair
    user: UserResponse
