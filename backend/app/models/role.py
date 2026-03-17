from __future__ import annotations

from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import DBBase
from core.database.mixins import PrimaryKeyMixin, TimestampMixin

if TYPE_CHECKING:
    from .user import DBUser


class DBRole(DBBase, PrimaryKeyMixin, TimestampMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(32), unique=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Relationship
    users: Mapped[List["DBUser"]] = relationship(
        secondary="user_roles", back_populates="roles"
    )

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"
