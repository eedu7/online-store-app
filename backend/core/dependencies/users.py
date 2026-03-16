from app.models import DBUser
from core.dependencies.auth import AuthenticationRequired
from core.dependencies.controllers import UserControllerDep


async def get_current_user(
    payload: AuthenticationRequired, controller: UserControllerDep
) -> DBUser:
    return await controller.get_by_id(payload.sub)
