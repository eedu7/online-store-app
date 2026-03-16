from uuid import UUID, uuid4

from sqlalchemy import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column


class PrimaryKeyMixin:
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        index=True,
        default=uuid4,
        sort_order=-10,
        primary_key=True,
    )
