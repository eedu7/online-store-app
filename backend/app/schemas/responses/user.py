from typing import List

from pydantic import UUID4, BaseModel, ConfigDict, EmailStr

from app.schemas.responses.role import RoleResponse


class UserResponse(BaseModel):
    id: UUID4
    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    profile_pic: str | None = None
    phone_number: str | None = None
    phone_verified: bool
    is_active: bool
    roles: List[RoleResponse] = []

    model_config = ConfigDict(from_attributes=True)
