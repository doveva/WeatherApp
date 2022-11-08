# Импорт классов для создания сервиса
from ..weather_service import WeatherBaseService
from .open_meteo_model import OpenMeteoModel

# Импорт датаклассов
from WeatherData.src.dataclasses.coordinates import Coordinates
from WeatherData.src.dataclasses.datetime_range import DateRange

# Импорт системных библиотек
from typing import List
import requests


class OpenMeteoService(WeatherBaseService):
    def __init__(self):
        self._url = 'https://api.open-meteo.com/v1/forecast'

    def get_day_data(self, coords: Coordinates) -> OpenMeteoModel:
        pass

    def get_period_data(self, coords: Coordinates, date_range: DateRange) -> List[OpenMeteoModel]:
        hour_data_string = ['dewpoint_2m', 'weathercode', 'cloudcover', 'windspeed_10m', 'windspeed_180m']
        params = {
            'latitude': coords.latitude,
            'longitude': coords.longitude,
            'hourly[]': hour_data_string,
            'start_date': date_range.start_date.strftime('%Y-%m-%d'),
            'end_date': date_range.end_date.strftime('%Y-%m-%d'),
            'timeformat': 'unixtime'
        }
        r = requests.get(self._url, params=params)
        data = r.json()
        print(data)
