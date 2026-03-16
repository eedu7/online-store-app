from uuid import UUID

from fastapi import APIRouter, Depends

from core.dependencies.auth import auth_required
from core.exceptions import NotImplementedException

router = APIRouter(dependencies=[Depends(auth_required)])


@router.get("/")
async def get_roles():

    raise NotImplementedException(
        message="Role listing endpoint not implemented",
        error_code="ROLE_LIST_NOT_IMPLEMENTED",
    )


@router.get("/{role_id}")
async def get_role_detial(role_id: UUID):

    raise NotImplementedException(
        message="Role detail endpoint not implemented",
        error_code="ROLE_DETAIL_NOT_IMPLEMENTED",
        details={"role_id": str(role_id)},
    )


@router.post("/")
async def add_role():

    raise NotImplementedException(
        message="Role creation endpoint not implemented",
        error_code="ROLE_CREATE_NOT_IMPLEMENTED",
    )


@router.put("/")
async def update_role():

    raise NotImplementedException(
        message="Role update endpoint not implemented",
        error_code="ROLE_UPDATE_NOT_IMPLEMENTED",
    )


@router.patch("/")
async def partial_update_role():

    raise NotImplementedException(
        message="Role partial update endpoint not implemented",
        error_code="ROLE_PARTIAL_UPDATE_NOT_IMPLEMENTED",
    )


@router.delete("/{role_id}")
async def remove_role(role_id: UUID):

    raise NotImplementedException(
        message="Role deletion endpoint not implemented",
        error_code="ROLE_DELETE_NOT_IMPLEMENTED",
        details={"role_id": str(role_id)},
    )
