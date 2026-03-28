from pydantic import BaseModel


class RoleBase(BaseModel):
    description: str | None = None

class RoleCreateRequest(RoleBase):
    name: str


class RoleUpdateRequest(RoleCreateRequest):
    pass


class RolePartialUpdateRequest(RoleBase):
    name: str | None = None
