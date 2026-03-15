from fastapi import APIRouter, Depends

from app.schemas.requests.auth import UserLoginRequest, UserRegisterRequest
from core.dependencies.auth import auth_required
from core.dependencies.controllers import AuthControllerDep
from core.exceptions import NotImplementedException

router = APIRouter()


@router.post("/register")
async def register(payload: UserRegisterRequest, controller: AuthControllerDep):
    return await controller.register(payload)


@router.post("/login")
async def login(payload: UserLoginRequest, controller: AuthControllerDep):
    return await controller.login(payload)


@router.post("/logout", dependencies=[Depends(auth_required)])
async def logout(controller: AuthControllerDep):
    raise NotImplementedException(
        message="User logout is not yet implemented",
        error_code="LOGOUT_NOT_IMPLEMENTED",
    )
