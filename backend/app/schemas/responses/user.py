from pydantic import UUID4, BaseModel, ConfigDict, EmailStr


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

    model_config = ConfigDict(from_attributes=True)
