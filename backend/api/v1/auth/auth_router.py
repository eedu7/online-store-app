from fastapi import APIRouter

from app.schemas.auth import UserLoginRequest, UserRegisterRequest
from core.dependencies.controllers import AuthControllerDep
from core.exceptions import NotImplementedException

router = APIRouter()


@router.post("/register")
async def register(payload: UserRegisterRequest, controller: AuthControllerDep):
    return await controller.regsiter(payload)
    raise NotImplementedException(
        message="User registration is not yet implemented",
        error_code="REGISTER_NOT_IMPLEMENTED",
    )


@router.post("/login")
async def login(payload: UserLoginRequest, controller: AuthControllerDep):
    raise NotImplementedException(
        message="User login is not yet implemented", error_code="LOGIN_NOT_IMPLEMENTED"
    )


@router.post("/logout")
async def logout(controller: AuthControllerDep):
    raise NotImplementedException(
        message="User logout is not yet implemented",
        error_code="LOGOUT_NOT_IMPLEMENTED",
    )
