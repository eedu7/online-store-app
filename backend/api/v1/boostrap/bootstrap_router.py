from typing import Annotated

from fastapi import APIRouter, Path

from app.schemas.requests.boostrap import SuperuserInRequest
from core.dependencies.bootstrap import SuperuserBoostrapDep

router = APIRouter()


@router.post("/superuser/{secret}")
async def create_superuser(
    secret: Annotated[str, Path(min_lenght=8, max_length=32)],
    payload: SuperuserInRequest,
    bootstrap: SuperuserBoostrapDep,
):
    return await bootstrap.create_superuser(payload, secret=secret)
