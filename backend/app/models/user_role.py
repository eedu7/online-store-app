from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.database import DBBase
from core.database.mixins import TimestampMixin


class DBUserRole(DBBase, TimestampMixin):
    __tablename__ = "user_roles"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"), primary_key=True)

    def __repr__(self) -> str:
        return f"UserRole(user_id={self.user_id!r}, role_id={self.role_id!r})"
