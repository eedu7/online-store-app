from typing import Annotated, Callable, cast
from uuid import UUID

from fastapi import Depends, HTTPException, status

from app.models import DBUser
from core.dependencies.auth import AuthenticationRequired
from core.dependencies.controllers import UserControllerDep
from core.exceptions import PermissionDeniedException


async def get_current_user(
    payload: AuthenticationRequired, controller: UserControllerDep
) -> DBUser:
    return await controller.get_by_id(cast(UUID, payload.sub))


CurrentUserDep = Annotated[DBUser, Depends(get_current_user)]


def _require_roles(*allowed_roles: str):
    """Factory that returns a dependency enforcing at least one matching role."""

    async def role_checker(user: CurrentUserDep) -> DBUser:
        user_role_names = {role.name for role in user.roles}
        if not user_role_names.intersection(allowed_roles):
            raise PermissionDeniedException()
        return user

    return role_checker


AdminUserDep = Annotated[DBUser, Depends(_require_roles("admin"))]
TenantUserDep = Annotated[DBUser, Depends(_require_roles("tenant"))]
StaffUserDep = Annotated[DBUser, Depends(_require_roles("staff"))]
