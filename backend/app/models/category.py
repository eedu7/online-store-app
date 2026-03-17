from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.database import DBBase
from core.database.mixins import AuditMixin, PrimaryKeyMixin, TimestampMixin

if TYPE_CHECKING:
    pass


class DBCategory(DBBase, PrimaryKeyMixin, TimestampMixin, AuditMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(32), unique=True)
    slug: Mapped[str] = mapped_column(String(48), unique=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r}, slug={self.slug!r})"
