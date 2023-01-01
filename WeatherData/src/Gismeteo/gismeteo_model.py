from Models.base_model import BaseMeteoModel
from datetime import datetime


class GismeteoModel(BaseMeteoModel):
    Humidity: int
    Weather: str
    CloudCover: int
    WindSpeed: float
    WindDirection: int
    Datetime: datetime

    @classmethod
    def create_model(cls, data: dict) -> BaseMeteoModel:
        result = {}
        return cls(**result)


class GismeteoMapper:
    @classmethod
    def weather_code(cls, data_code: dict) -> str:
        pass





