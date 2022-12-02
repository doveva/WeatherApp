from pydantic import BaseModel
from uuid import UUID, uuid4
from abc import abstractmethod
from typing import Optional


class BaseMeteoModel(BaseModel):
    Id: Optional[UUID] = uuid4()

    @abstractmethod
    def convert_to_json_dict(self) -> dict:
        pass
