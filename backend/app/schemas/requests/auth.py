import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserRegisterRequest(BaseModel):
    email: EmailStr = Field(
        ..., description="User's email address", examples=["john.doe@example.com"]
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Unique username",
        examples=["john_doe"],
    )
    password: str = Field(
        ..., min_length=8, description="Strong password", examples=["SecurePass123!"]
    )

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not re.match(r"^[a-zA-Z0-9_-]+$", v):
            raise ValueError(
                "Username can only contain letters, numbers, underscores (_), and hyphens (-)"
            )
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\"':{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        return v


class UserLoginRequest(BaseModel):
    username_or_email: str = Field(
        ...,
        description="Username or email address",
        examples=["john_doe", "john.doe@example.com"],
    )
    password: str = Field(..., description="User password", examples=["SecurePass123!"])


class UserLogoutRequest(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None
