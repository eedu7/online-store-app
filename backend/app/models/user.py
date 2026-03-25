from __future__ import annotations

from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import DBBase
from core.database.mixins import PrimaryKeyMixin, TimestampMixin

if TYPE_CHECKING:
    from .role import DBRole


class DBUser(DBBase, PrimaryKeyMixin, TimestampMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    email_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="false"
    )

    password: Mapped[str] = mapped_column(Text, nullable=True)

    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True)

    profile_pic: Mapped[str] = mapped_column(String(255), nullable=True)

    phone_number: Mapped[str] = mapped_column(String(32), nullable=True)
    phone_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="false"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true"
    )

    # Relationship
    roles: Mapped[List["DBRole"]] = relationship(
        secondary="user_roles", back_populates="users", lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
