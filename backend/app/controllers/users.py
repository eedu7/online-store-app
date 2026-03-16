from uuid import UUID

from app.models import DBUser
from app.repositories import UserRepository
from core.controller import BaseController
from core.exceptions import NotFoundException


class UserController(BaseController[DBUser]):
    def __init__(self, repository: UserRepository) -> None:
        super().__init__(DBUser, repository)
        self.repository: UserRepository = repository

    async def get_by_id(self, id: str | UUID) -> DBUser:
        user = await self.repository.get_by_id(UUID(id))

        if user is None:
            raise NotFoundException(
                message="User not found",
                error_code="USER_NOT_FOUND",
                details={"id": id},
            )

        return user

    async def get_by_username(self, username: str) -> DBUser:
        user = await self.repository.get_by_username(username)

        if user is None:
            raise NotFoundException(
                message="User not found",
                error_code="USER_NOT_FOUND",
                details={"username": username},
            )

        return user

    async def get_by_email(self, email: str) -> DBUser:
        user = await self.repository.get_by_email(email)

        if user is None:
            raise NotFoundException(
                message="User not found",
                error_code="USER_NOT_FOUND",
                details={"email": email},
            )

        return user
