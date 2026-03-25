from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RoleResponse(BaseModel):
    id: UUID
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)
