from pydantic import BaseModel, validator
from uuid import UUID, uuid4
from abc import abstractmethod
from typing import Optional


class BaseMeteoModel(BaseModel):
    Id: Optional[UUID]

    @abstractmethod
    def convert_to_json_dict(self) -> dict:
        pass

    @validator('Id', pre=True, always=True)
    def generate_uuid(cls, v):
        if v is None:
            v = uuid4()
        return v
