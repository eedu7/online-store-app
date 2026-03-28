from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.schemas.requests.role import (
    RoleCreateRequest,
    RolePartialUpdateRequest,
    RoleUpdateRequest,
)
from core.dependencies.auth import auth_required
from core.dependencies.controllers import RoleControllerDep

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
async def update_role(
    uid: UUID,
    payload: RoleUpdateRequest,
    controller: RoleControllerDep,
):
    return await controller.update_role(uid, payload)


@router.patch("/{uid}")
async def partial_update_role(
    uid: UUID, payload: RolePartialUpdateRequest, controller: RoleControllerDep
):
    return await controller.update_role(uid, payload)


@router.delete("/{uid}")
async def remove_role(uid: UUID, controller: RoleControllerDep):
    return await controller.delete_role(uid)
