from sqlalchemy.orm import Session

from app.models import DBUser
from core.repository import BaseRepository


class UserRepository(BaseRepository[DBUser]):
    def __init__(self, db: Session) -> None:
        super().__init__(DBUser, db)
