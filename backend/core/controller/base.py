from typing import Any, Dict, Generic, Sequence, Type, TypeVar
from uuid import UUID

from core.database import DBBase
from core.exceptions import NotFoundException
from core.repository import BaseRepository

T = TypeVar("T", bound=DBBase)


class BaseController(Generic[T]):
    def __init__(self, model: Type[T], repository: BaseRepository) -> None:
        self.model = model
        self.repository = repository

    async def get_by_id(self, id: UUID) -> T:
        db_obj = await self.repository.get_by_id(id)
        if db_obj is None:
            raise NotFoundException()
        return db_obj

    async def get_one_by_filters(self, filters: Dict[str, Any]) -> T | None:
        return await self.repository.get_one_by_filters(filters)

    async def get_one_or_fail(self, filters: Dict[str, Any]) -> T:
        db_obj = await self.repository.get_one_by_filters(filters)
        if db_obj is None:
            raise NotFoundException()
        return db_obj

    async def get_all(self, skip: int = 0, limit: int | None = None) -> Sequence[T]:
        return await self.repository.get_all(skip=skip, limit=limit)

    async def exists(self, id: UUID) -> bool:
        db_obj = await self.repository.get_by_id(id)
        return db_obj is not None

    async def commit(self) -> None:
        await self.repository.commit()

    async def refresh(self, db_obj: T) -> T:
        return await self.repository.refresh(db_obj)

    async def flush(self) -> None:
        await self.repository.flush()

    async def rollback(self) -> None:
        await self.repository.rollback()
