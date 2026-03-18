from typing import Annotated

from fastapi import APIRouter, Path, status

from app.schemas.requests.boostrap import SuperuserInRequest
from app.schemas.responses.auth import AuthResponse
from core.dependencies.bootstrap import SuperuserBoostrapDep

router = APIRouter()


@router.post(
    "/superuser/{secret}",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Bootstrap Superuser",
    description="Create the initial superuser account. Can only be used once.",
)
async def create_superuser(
    secret: Annotated[
        str,
        Path(
            ...,
            min_lenght=8,
            max_length=128,
            description="Bootstrap secret for system initialization",
        ),
    ],
    payload: SuperuserInRequest,
    bootstrap: SuperuserBoostrapDep,
):
    return await bootstrap.create_superuser(payload=payload, secret=secret)
