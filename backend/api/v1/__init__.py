from fastapi import APIRouter

from .auth import router as auth_router
from .boostrap import router as bootstrap_router
from .role import router as role_router
from .users import router as user_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(user_router, prefix="/user", tags=["User Management"])
router.include_router(role_router, prefix="/role", tags=["Role Management"])
router.include_router(bootstrap_router, prefix="/bootstrap", tags=["Bootstrap"])
