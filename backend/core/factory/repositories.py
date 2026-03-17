from typing import Annotated

from fastapi import Depends

from app.repositories import RoleRepository, UserRepository, UserRoleRepository
from core.dependencies.session import AsyncSessionDep


class RepositoryFactory:
    @staticmethod
    def get_user_repository(session: AsyncSessionDep) -> UserRepository:
        return UserRepository(session)

    @staticmethod
    def get_role_repository(session: AsyncSessionDep) -> RoleRepository:
        return RoleRepository(session)

    @staticmethod
    def get_user_role_repository(session: AsyncSessionDep) -> UserRoleRepository:
        return UserRoleRepository(session)


UserRepositoryDep = Annotated[
    UserRepository, Depends(RepositoryFactory.get_user_repository)
]

RoleRepositoryDep = Annotated[
    RoleRepository, Depends(RepositoryFactory.get_role_repository)
]

UserRoleRepositoryDep = Annotated[
    UserRoleRepository, Depends(RepositoryFactory.get_user_role_repository)
]
