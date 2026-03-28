from app.models import DBRole
from app.repositories import RoleRepository
from core.controller import BaseController


class RoleController(BaseController[DBRole]):
    def __init__(self, repository: RoleRepository) -> None:
        super().__init__(DBRole, repository)

    async def create_role(self):
        pass

    async def update_role(self):
        pass

    async def delete_role(self):
        pass
