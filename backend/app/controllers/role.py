from app.models import DBRole, DBUser
from app.repositories import RoleRepository
from app.schemas.requests.role import RoleCreateRequest
from core.controller import BaseController
from core.exceptions import BadRequestException


class RoleController(BaseController[DBRole]):
    def __init__(self, repository: RoleRepository) -> None:
        super().__init__(DBRole, repository)
        self.repository = repository

    async def create_role(
        self,
        payload: RoleCreateRequest,
        user: DBUser,
    ):
        try:
            return await self.repository.create(
                {
                    **payload.model_dump(),
                    "created_by": user.id,
                    "updated_by": user.id,
                }
            )
        except Exception as exc:
            raise BadRequestException(details={"role": str(exc)})

    async def update_role(self):
        pass

    async def delete_role(self):
        pass
