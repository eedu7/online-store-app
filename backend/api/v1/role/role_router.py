from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.schemas.requests.role import RoleCreateRequest
from core.dependencies.auth import auth_required
from core.dependencies.controllers import RoleControllerDep
from core.dependencies.users import AdminUserDep
from core.exceptions import NotImplementedException

router = APIRouter(dependencies=[Depends(auth_required)])


@router.get("/")
async def get_roles(
    controller: RoleControllerDep,
    skip: int = 0,
    limit: int = 100,
):
    return await controller.get_all(skip=skip, limit=limit)


@router.get("/{uid}")
async def get_role_detail(uid: UUID, controller: RoleControllerDep):
    return await controller.get_by_id(uid)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_role(payload: RoleCreateRequest, controller: RoleControllerDep):
    return await controller.create_role(payload)


@router.put("/{uid}")
async def update_role(uid: UUID, admin: AdminUserDep, controller: RoleControllerDep):

    raise NotImplementedException(
        message="Role update endpoint not implemented",
        error_code="ROLE_UPDATE_NOT_IMPLEMENTED",
    )


@router.patch("/{uid}")
async def partial_update_role(
    uid: UUID, user: AdminUserDep, controller: RoleControllerDep
):

    raise NotImplementedException(
        message="Role partial update endpoint not implemented",
        error_code="ROLE_PARTIAL_UPDATE_NOT_IMPLEMENTED",
    )


@router.delete("/{uid}")
async def remove_role(uid: UUID, controller: RoleControllerDep):
    return await controller.delete_role(uid)
