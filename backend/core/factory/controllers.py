from app.controllers import AuthController, RoleController, UserController
from app.repositories import RoleRepository
from core.factory.repositories import (
    UserRepositoryDep,
)
from core.security import PasswordServiceDep
from core.security.jwt import JWTServiceDep


class ControllerFactory:
    @staticmethod
    def get_user_controller(repository: UserRepositoryDep) -> UserController:
        return UserController(repository=repository)

    @staticmethod
    def get_auth_controller(
        repository: UserRepositoryDep,
        jwt_service: JWTServiceDep,
        password_service: PasswordServiceDep,
    ) -> AuthController:
        return AuthController(
            repository=repository,
            jwt_service=jwt_service,
            password_service=password_service,
        )

    @staticmethod
    def get_roll_controller(
        repository: RoleRepository,
    ) -> RoleController:
        return RoleController(repository=repository)
