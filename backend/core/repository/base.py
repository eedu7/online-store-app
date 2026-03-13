from typing import Any, Dict, Generic, List, Type, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import DBBase

T = TypeVar("T", bound=DBBase)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get_by_id(self, id: UUID) -> T | None:
        return await self.session.get(self.model, id)

    async def get_all(self, skip: int = 0, limit: int = 20) -> List[T]:
        raise NotImplementedError

    async def get_by_filters(self, filters: Dict[str, Any]) -> List[T]:
        raise NotImplementedError

    async def get_one_by_filters(self, filters: Dict[str, Any]) -> T | None:
        raise NotImplementedError

    async def create(self, obj_in: Dict[str, Any]) -> T:
        raise NotImplementedError

    async def update(self, id: UUID, obj_in: Dict[str, Any]) -> T | None:
        raise NotImplementedError

    async def delete(self, id: UUID) -> bool:
        raise NotImplementedError
