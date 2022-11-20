# Импорт классов для создания сервиса
from ..weather_service import WeatherBaseService
from .open_meteo_model import OpenMeteoModel, OpenWeatherMapper

# Импорт датаклассов
from ..Utils.coordinates import Coordinates
from ..Utils.datetime_range import DateRange

# Импорт системных библиотек
from typing import List
import requests

from http import HTTPStatus


class OpenMeteoService(WeatherBaseService):
    def __init__(self):
        self._url = 'https://api.open-meteo.com/v1/forecast'

    def get_day_data(self, coords: Coordinates) -> OpenMeteoModel:
        pass

    def get_period_data(self, coords: Coordinates, date_range: DateRange) -> List[OpenMeteoModel]:
        hour_data_string = OpenWeatherMapper.get_params
        params = {
            'latitude': coords.latitude,
            'longitude': coords.longitude,
            'hourly[]': hour_data_string,
            'start_date': date_range.start_date.strftime('%Y-%m-%d'),
            'end_date': date_range.end_date.strftime('%Y-%m-%d'),
            'timeformat': 'unixtime'
        }
        r = requests.get(self._url, params=params)
        if r.status_code == HTTPStatus.OK:
            data = r.json()['hourly']
            # Mappers creation
            data_keys = tuple(data.keys())
            model_keys = {}
            for key, value in OpenWeatherMapper.mapper.items():
                model_keys[value] = key

            result = []
            for data_num in range(len(data['time'])):
                data_row = {}
                for key in data_keys:
                    data_row[model_keys[key]] = data[key][data_num]
                result.append(OpenMeteoModel(**data_row))

            return result
        return []
