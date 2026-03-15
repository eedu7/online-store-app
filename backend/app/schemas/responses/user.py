from pydantic import UUID4, BaseModel, ConfigDict, EmailStr


class UserResponse(BaseModel):
    id: UUID4
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
