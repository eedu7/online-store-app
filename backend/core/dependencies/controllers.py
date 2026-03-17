from typing import Annotated

from fastapi import Depends

from app.controllers import AuthController, RoleController, UserController
from core.factory import ControllerFactory

UserControllerDep = Annotated[
    UserController, Depends(ControllerFactory.get_user_controller)
]
AuthControllerDep = Annotated[
    AuthController, Depends(ControllerFactory.get_auth_controller)
]
RoleControllerDep = Annotated[
    RoleController, Depends(ControllerFactory.get_roll_controller)
]
