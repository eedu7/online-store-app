from uuid import UUID, uuid4

from sqlalchemy import UUID as PG_UUID
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.database import DBBase


class DBUser(DBBase):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r})"
