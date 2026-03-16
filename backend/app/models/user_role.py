from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import DBBase
from core.database.mixins import PrimaryKeyMixin, TimestampMixin

if TYPE_CHECKING:
    from .role import DBRole
    from .user import DBUser


class DBUserRole(DBBase, PrimaryKeyMixin, TimestampMixin):
    __tablename__ = "user_roles"

    # Foreign Keys
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    role_id: Mapped[UUID] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Relation
    user: Mapped["DBUser"] = relationship(
        "DBUser", foreign_keys=[user_id], back_populates="user_roles"
    )
    role: Mapped["DBRole"] = relationship(
        "DBRole", foreign_keys=[role_id], back_populates="user_roles"
    )

    __table_args__ = (UniqueConstraint("user_id", "role_id", name="uq_user_role"),)

    def __repr__(self) -> str:
        return f"UserRole(ID: {self.id})"
