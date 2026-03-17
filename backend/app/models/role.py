from __future__ import annotations

from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.user_role import DBUserRole
from core.database import DBBase
from core.database.mixins import AuditMixin, PrimaryKeyMixin, TimestampMixin

if TYPE_CHECKING:
    from .user_role import DBUserRole


class DBRole(DBBase, PrimaryKeyMixin, TimestampMixin, AuditMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Relations
    user_roles: Mapped[List["DBUserRole"]] = relationship(
        "DBUserRole", back_populates="role", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"
