from fastapi import APIRouter, Depends, Request, Response, status

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
async def register(
    response: Response, payload: UserRegisterRequest, controller: AuthControllerDep
):
    return await controller.register(payload, response)


@router.post("/login", response_model=AuthResponse, status_code=status.HTTP_200_OK)
async def login(
    response: Response,
    payload: UserLoginRequest,
    controller: AuthControllerDep,
):
    return await controller.login(payload, response)


@router.post(
    "/logout",
    dependencies=[Depends(auth_required)],
    status_code=status.HTTP_200_OK,
)
async def logout(
    request: Request, payload: UserLogoutRequest, controller: AuthControllerDep
):
    await controller.logout(payload, request)
    return {
        "statusCode": status.HTTP_200_OK,
        "success": True,
        "message": "Successfully logged out",
    }
