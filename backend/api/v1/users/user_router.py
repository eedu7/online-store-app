from fastapi import APIRouter, Depends

from core.dependencies.auth import auth_required

router = APIRouter(dependencies=[Depends(auth_required)])


@router.get("/")
async def get_user():
    pass
