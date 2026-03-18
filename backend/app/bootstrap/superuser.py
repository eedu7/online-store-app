from app.models import DBUser
from app.repositories import RoleRepository, UserRepository, UserRoleRepository
from core.controller import BaseController
from core.security import PasswordService
from core.security.jwt import JWTService


class SuperuserBootstrap(BaseController[DBUser]):
    def __init__(
        self,
        user_repository: UserRepository,
        user_role_repository: UserRoleRepository,
        role_repository: RoleRepository,
        jwt_service: JWTService,
        password_service: PasswordService,
    ) -> None:
        super().__init__(DBUser, user_repository)
        self.user_repository = user_repository
        self.user_role_repository = user_role_repository
        self.role_repository = role_repository
        self.jwt_service = jwt_service
        self.password_service = password_service
