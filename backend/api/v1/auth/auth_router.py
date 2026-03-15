from fastapi import APIRouter, Depends, status

from app.schemas.requests.auth import UserLoginRequest, UserRegisterRequest
from app.schemas.responses.auth import AuthResponse
from core.dependencies.auth import auth_required
from core.dependencies.controllers import AuthControllerDep
from core.exceptions import NotImplementedException

router = APIRouter()


@router.post(
    "/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED
)
async def register(payload: UserRegisterRequest, controller: AuthControllerDep):
    return await controller.register(payload)


@router.post("/login", response_model=AuthResponse, status_code=status.HTTP_200_OK)
async def login(payload: UserLoginRequest, controller: AuthControllerDep):
    return await controller.login(payload)


@router.post(
    "/logout",
    dependencies=[Depends(auth_required)],
)
async def logout(controller: AuthControllerDep):
    raise NotImplementedException(
        message="User logout is not yet implemented",
        error_code="LOGOUT_NOT_IMPLEMENTED",
    )
