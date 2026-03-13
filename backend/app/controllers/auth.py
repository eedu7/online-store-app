from app.models import DBUser
from app.repositories import UserRepository
from app.schemas.auth import UserRegisterRequest
from core.controller import BaseController


class AuthController(BaseController[DBUser]):
    def __init__(self, repository: UserRepository) -> None:
        super().__init__(DBUser, repository)
        self.repository = repository

    async def regsiter(self, payload: UserRegisterRequest) -> DBUser:
        user = await self.repository.create({**payload.model_dump()})
        await self.commit()
        return user
