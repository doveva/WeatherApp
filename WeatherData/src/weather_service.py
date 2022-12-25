from abc import abstractmethod
from Utils.coordinates import Place
from Utils.datetime_range import DateRange
from typing import List


class WeatherBaseService:
    """
    Базовый интерфейс для получения данных от источника
    """
    __name__ = NotImplementedError

    @abstractmethod
    def get_day_json_data(self, coords: Place) -> dict:
        pass

    @abstractmethod
    def get_period_json_data(self, coords: Place, date_range: DateRange) -> List[dict]:
        pass

    def __str__(self):
        return self.__name__
