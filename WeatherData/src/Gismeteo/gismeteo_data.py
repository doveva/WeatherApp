import datetime

from Core.settings import config

from weather_service import WeatherBaseService

from Models.base_model import BaseMeteoModel
from Gismeteo.gismeteo_model import GismeteoModel

from Utils.coordinates import Place
from Utils.datetime_range import DateRange

from typing import List
import requests
from http import HTTPStatus


class GismeteoService(WeatherBaseService):
    __name__ = 'Gismeteo Service'

    def __init__(self):
        self._url = 'https://api.gismeteo.net/v2/weather/forecast/4368/'

    def get_day_json_data(self, coords: Place) -> dict:
        pass

    def _get_period_data(self, coords: Place, date_range: DateRange) -> List[BaseMeteoModel]:
        result = []
        diff = date_range.end_date - datetime.date.today()
        if 0 < diff.days <= 10:
            response = requests.get(
                url=self._url,
                params={
                    'latitude': coords.latitude,
                    'longitude': coords.longitude,
                    'lang': 'en',
                    'days': diff.days
                },
                headers={
                    'X-Gismeteo-Token': config.GISMETEO_TOKEN,
                    'Accept-Encoding': 'gzip'
                }
            )
            if response.status_code == HTTPStatus.OK:
                data = response.json()['response']
                for data_row in data:
                    result.append(GismeteoModel.create_model(data_row))
        return result

    def get_period_json_data(self, coords: Place, date_range: DateRange) -> List[dict]:
        result = []
        for data_value in self._get_period_data(coords=coords, date_range=date_range):
            result.append(data_value.convert_to_json_dict())
        return result
