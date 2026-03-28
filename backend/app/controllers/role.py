from uuid import UUID

from app.models import DBRole, DBUser
from app.repositories import RoleRepository
from app.schemas.requests.role import (
    RoleCreateRequest,
    RolePartialUpdateRequest,
    RoleUpdateRequest,
)
from core.controller import BaseController
from core.exceptions import BadRequestException, NotFoundException


class RoleController(BaseController[DBRole]):
    def __init__(self, repository: RoleRepository) -> None:
        super().__init__(DBRole, repository)
        self.repository = repository

    async def create_role(
        self,
        payload: RoleCreateRequest,
    ):
        try:
            role = await self.repository.create(
                payload.model_dump(),
            )
            await self.commit()
            return role

        except Exception as exc:
            raise BadRequestException(details={"role": str(exc)})

    async def update_role(
        self,
        id: UUID,
        payload: RoleUpdateRequest | RolePartialUpdateRequest,
    ):
        role = await self.repository.get_by_id(id)

        if role is None:
            raise NotFoundException(details={"role": str(id)})

        updated = await self.repository.update(
            role, payload.model_dump(exclude_none=True)
        )
        await self.commit()
        return updated

    async def delete_role(self, id: UUID) -> None:
        role = await self.repository.get_by_id(id)

        if role is None:
            raise NotFoundException(details={"role": str(id)})
        try:
            await self.repository.delete(role)

            await self.commit()
        except Exception as exc:
            raise BadRequestException(details={"role": str(exc)})
