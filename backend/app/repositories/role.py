from sqlalchemy.ext.asyncio import AsyncSession

from app.models import DBRole
from core.repository import BaseRepository


class RoleRepository(BaseRepository[DBRole]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(DBRole, session)
