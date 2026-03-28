from uuid import UUID

from fastapi import APIRouter, Depends

from core.dependencies.auth import auth_required
from core.dependencies.users import AdminUserDep
from core.exceptions import NotImplementedException

router = APIRouter(dependencies=[Depends(auth_required)])


@router.get("/")
async def get_roles():

    raise NotImplementedException(
        message="Role listing endpoint not implemented",
        error_code="ROLE_LIST_NOT_IMPLEMENTED",
    )


@router.get("/{uid}")
async def get_role_detail(
    uid: UUID,
):

    raise NotImplementedException(
        message="Role detail endpoint not implemented",
        error_code="ROLE_DETAIL_NOT_IMPLEMENTED",
        details={"uid": str(uid)},
    )


@router.post("/")
async def add_role(admin: AdminUserDep):

    raise NotImplementedException(
        message="Role creation endpoint not implemented",
        error_code="ROLE_CREATE_NOT_IMPLEMENTED",
    )


@router.put("/{uid}")
async def update_role(uid: UUID, admin: AdminUserDep):

    raise NotImplementedException(
        message="Role update endpoint not implemented",
        error_code="ROLE_UPDATE_NOT_IMPLEMENTED",
    )


@router.patch("/{uid}")
async def partial_update_role(uid: UUID, user: AdminUserDep):

    raise NotImplementedException(
        message="Role partial update endpoint not implemented",
        error_code="ROLE_PARTIAL_UPDATE_NOT_IMPLEMENTED",
    )


@router.delete("/{uid}")
async def remove_role(uid: UUID, admin: AdminUserDep):

    raise NotImplementedException(
        message="Role deletion endpoint not implemented",
        error_code="ROLE_DELETE_NOT_IMPLEMENTED",
        details={"uid": str(uid)},
    )
