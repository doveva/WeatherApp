from abc import abstractmethod
from .Utils.coordinates import Coordinates
from .Utils.datetime_range import DateRange
from pydantic import BaseModel
from typing import List


class WeatherBaseService:
    """
    Базовый интерфейс для получения данных от источника
    """
    @abstractmethod
    def get_day_data(self, coords: Coordinates) -> BaseModel:
        pass

    @abstractmethod
    def get_period_data(self, coords: Coordinates, data_range: DateRange) -> List[BaseModel]:
        pass
