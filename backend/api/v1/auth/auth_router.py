from fastapi import APIRouter, Depends, status

from app.schemas.requests.auth import (
    UserLoginRequest,
    UserLogoutRequest,
    UserRegisterRequest,
)
from app.schemas.responses.auth import AuthResponse
from core.dependencies.auth import auth_required
from core.dependencies.controllers import AuthControllerDep

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
    status_code=status.HTTP_204_NO_CONTENT,
)
async def logout(payload: UserLogoutRequest, controller: AuthControllerDep):
    await controller.logout(payload)
