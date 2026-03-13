from fastapi import APIRouter

from core.exceptions import NotImplementedException

router = APIRouter()


@router.post("/register")
async def register():
    raise NotImplementedException(
        message="User registration is not yet implemented",
        error_code="REGISTER_NOT_IMPLEMENTED",
    )


@router.post("/login")
async def login():
    raise NotImplementedException(
        message="User login is not yet implemented", error_code="LOGIN_NOT_IMPLEMENTED"
    )


@router.post("/logout")
async def logout():
    raise NotImplementedException(
        message="User logout is not yet implemented",
        error_code="LOGOUT_NOT_IMPLEMENTED",
    )
