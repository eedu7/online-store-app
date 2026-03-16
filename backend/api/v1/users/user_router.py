from fastapi import APIRouter, Depends

from core.dependencies.auth import auth_required
from core.dependencies.users import get_current_user

router = APIRouter(dependencies=[Depends(auth_required)])


@router.get("/me")
async def get_user(payload=Depends(get_current_user)):
    return {"payload": payload}
