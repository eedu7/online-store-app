from typing import Annotated

from fastapi import Depends

from app.controllers import AuthController, UserController
from app.repositories import UserRepository
from core.factory.repositories import RepositoryFactory

UserRepositoryDep = Annotated[
    UserRepository, Depends(RepositoryFactory.get_user_repository)
]


class ControllerFactory:
    @staticmethod
    def get_user_controller(repository: UserRepositoryDep) -> UserController:
        return UserController(repository=repository)

    @staticmethod
    def get_auth_controller(repository: UserRepositoryDep) -> AuthController:
        return AuthController(repository=repository)
