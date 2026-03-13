from sqlalchemy.ext.asyncio import AsyncSession

from app.models import DBUser
from core.repository import BaseRepository


class UserRepository(BaseRepository[DBUser]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(DBUser, db)
