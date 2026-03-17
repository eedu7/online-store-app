from typing import Annotated

from fastapi import Depends

from app.repositories import UserRepository
from core.dependencies.session import AsyncSessionDep


class RepositoryFactory:
    @staticmethod
    def get_user_repository(session: AsyncSessionDep) -> UserRepository:
        return UserRepository(session)


UserRepositoryDep = Annotated[
    UserRepository, Depends(RepositoryFactory.get_user_repository)
]
