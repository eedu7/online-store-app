from fastapi import APIRouter, Depends, Request

from core.dependencies.auth import auth_required
from core.dependencies.users import get_current_user

router = APIRouter(dependencies=[Depends(auth_required)])


@router.get("/me")
async def get_user(request: Request, user=Depends(get_current_user)):

    return {"user": user, "cookies": request.cookies}
