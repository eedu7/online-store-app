from fastapi import APIRouter

from core.dependencies.bootstrap import SuperuserBoostrapDep

router = APIRouter()


@router.post("/superuser/{secret}")
async def create_superuser(secret: str, bootstrap: SuperuserBoostrapDep):
    pass
