from pydantic import BaseModel
from uuid import UUID


class OpenMeteoModel(BaseModel):
    id: UUID
