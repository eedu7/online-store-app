from app.models import DBRole
from app.repositories import RoleRepository
from core.controller import BaseController


class RoleController(BaseController[DBRole]):
    def __init__(self, repository: RoleRepository) -> None:
        super().__init__(DBRole, repository)
