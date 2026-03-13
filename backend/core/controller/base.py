from typing import Generic, Type, TypeVar
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
