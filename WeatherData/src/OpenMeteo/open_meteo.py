from ..weather_service import WeatherBaseService
from WeatherData.src.dataclasses.coordinates import Coordinates
from WeatherData.src.dataclasses.datetime_range import DateRange
from .open_meteo_model import OpenMeteoModel
from typing import List


class OpenMeteoService(WeatherBaseService):
    def __init__(self):
        self._url = 'https://api.open-meteo.com/v1/forecast'

    def get_day_data(self, coords: Coordinates) -> OpenMeteoModel:
        pass

    def get_period_data(self, coords: Coordinates, date_range: DateRange) -> List[OpenMeteoModel]:
        pass
