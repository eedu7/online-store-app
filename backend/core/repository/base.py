from typing import Any, Dict, Generic, List, Type, TypeVar
from uuid import UUID

from sqlalchemy.orm import DeclarativeMeta, Session

T = TypeVar("T", bound=DeclarativeMeta)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], db: Session) -> None:
        self.model = model
        self.db = db

    def get_by_id(self, id: UUID) -> T | None:
        raise NotImplementedError

    def get_all(self, skip: int = 0, limit: int = 20) -> List[T]:
        raise NotImplementedError

    def get_by_filters(self, filters: Dict[str, Any]) -> List[T]:
        raise NotImplementedError

    def get_one_by_filters(self, filters: Dict[str, Any]) -> T | None:
        raise NotImplementedError

    def create(self, obj_in: Dict[str, Any]) -> T:
        raise NotImplementedError

    def update(self, id: UUID, obj_in: Dict[str, Any]) -> T | None:
        raise NotImplementedError

    def delete(self, id: UUID) -> bool:
        raise NotImplementedError
