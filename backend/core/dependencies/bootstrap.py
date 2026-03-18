from typing import Annotated

from fastapi import Depends

from app.bootstrap import SuperuserBootstrap
from core.factory.repositories import (
    RoleRepositoryDep,
    UserRepositoryDep,
    UserRoleRepositoryDep,
)
from core.security import PasswordServiceDep
from core.security.jwt import JWTServiceDep


class BootstrapDependency:
    @staticmethod
    def get_superuser_bootstrap(
        user_repository: UserRepositoryDep,
        user_role_repository: UserRoleRepositoryDep,
        role_repository: RoleRepositoryDep,
        password_service: PasswordServiceDep,
        jwt_service: JWTServiceDep,
    ) -> SuperuserBootstrap:
        return SuperuserBootstrap(
            user_repository=user_repository,
            user_role_repository=user_role_repository,
            role_repository=role_repository,
            jwt_service=jwt_service,
            password_service=password_service,
        )


SuperuserBoostrapDep = Annotated[
    SuperuserBootstrap, Depends(BootstrapDependency.get_superuser_bootstrap)
]
