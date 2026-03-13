from typing import Any, Dict, Generic, Mapping, Sequence, Type, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import DBBase

T = TypeVar("T", bound=DBBase)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get_by_id(self, id: UUID) -> T | None:
        return await self.session.get(self.model, id)

    async def get_all(self, skip: int = 0, limit: int = 20) -> Sequence[T]:
        return await self.get_by_filters(skip=skip, limit=limit)

    async def get_by_filters(
        self, skip: int = 0, limit: int = 100, filters: Dict[str, Any] | None = None
    ) -> Sequence[T]:
        stmt = select(self.model)

        stmt = self._apply_filters(stmt, filters)

        stmt = stmt.offset(skip).limit(limit)

        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_one_by_filters(self, filters: Dict[str, Any]) -> T | None:
        stmt = select(self.model)
        stmt = self._apply_filters(stmt, filters)

        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, obj_in: T) -> T:
        self.session.add(obj_in)
        await self.session.refresh(obj_in)
        return obj_in

    async def update(self, db_obj: T, obj_in: Dict[str, Any]) -> T | None:
        for key, value in obj_in.items():
            if hasattr(db_obj, key):
                setattr(db_obj, key, value)
        await self.session.refresh(db_obj)
        return db_obj

    async def delete(self, db_obj: T) -> bool:
        await self.session.delete(db_obj)
        return True

    def _apply_filters(self, stmt, filters: Mapping[str, Any] | None = None):
        if filters is None:
            return stmt

        for field, value in filters.items():
            column = getattr(self.model, field, None)

            if column is None:
                raise AttributeError(
                    f"Model {self.model.__name__} has no attribute '{field}'"
                )
            if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
                stmt = stmt.where(column.in_(value))
            else:
                stmt = stmt.where(column == value)
        return stmt
