from app.controllers import AuthController, RoleController, UserController
from core.factory.repositories import (
    RoleRepositoryDep,
    UserRepositoryDep,
)


class ControllerFactory:
    @staticmethod
    def get_user_controller(repository: UserRepositoryDep) -> UserController:
        return UserController(repository=repository)

    @staticmethod
    def get_auth_controller(repository: UserRepositoryDep) -> AuthController:
        return AuthController(repository=repository)

    @staticmethod
    def get_role_controller(repository: RoleRepositoryDep) -> RoleController:
        return RoleController(repository=repository)
