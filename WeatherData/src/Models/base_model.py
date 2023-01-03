from pydantic import BaseModel, validator
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime

from Utils.timezones import spb_timezone


class BaseMeteoModel(BaseModel):
    Id: Optional[UUID]

    @validator('Id', pre=True, always=True)
    def generate_uuid(cls, v):
        if v is None:
            v = uuid4()
        return v

    def convert_to_json_dict(self) -> dict:
        data = self.dict()
        for key, value in data.items():
            if isinstance(value, UUID):
                data[key] = str(value)
            if isinstance(value, datetime):
                data[key] = value.replace(tzinfo=spb_timezone).replace(microsecond=0).isoformat()
        return data

