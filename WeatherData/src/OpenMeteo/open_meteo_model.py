import json
from pydantic import validator
from datetime import datetime
from uuid import UUID


from ..Utils.status_codes import WeatherStatusCodes
from ..Models.base_model import BaseMeteoModel


class OpenMeteoModel(BaseMeteoModel):
    dewpoint: float
    weather: str
    cloud_cover: int
    wind_speed_low: float
    wind_direction_low: str = None
    wind_speed_high: float = None
    wind_direction_high: str = None
    datetime: datetime

    @validator('weather', pre=True)
    def validate_weather(cls, v):
        return OpenWeatherMapper.weather_code(v)

    def convert_to_json_dict(self) -> dict:
        data = self.dict()
        for key, value in data.items():
            if isinstance(value, UUID):
                data[key] = value.hex
            if isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data


class OpenWeatherMapper:
    get_params = [
        'dewpoint_2m',
        'weathercode',
        'cloudcover',
        'windspeed_10m',
        'winddirection_10m',
        'windspeed_180m',
        'winddirection_180m'
    ]

    mapper = {
        'datetime': 'time',
        'dewpoint': 'dewpoint_2m',
        'weather': 'weathercode',
        'cloud_cover': 'cloudcover',
        'wind_speed_low': 'windspeed_10m',
        'wind_direction_low': 'winddirection_10m',
        'wind_speed_high': 'windspeed_180m',
        'wind_direction_high': 'winddirection_180m',
    }

    @staticmethod
    def weather_code(code: int) -> str | None:
        match code:

            case 0:
                return WeatherStatusCodes.clear
            case 1:
                return WeatherStatusCodes.mainly_clear
            case 2:
                return WeatherStatusCodes.partly_cloudy
            case 3:
                return WeatherStatusCodes.overcast
            case [45, 48]:
                return WeatherStatusCodes.fog
            case [51, 53, 55]:
                return WeatherStatusCodes.drizzle
            case [56, 57]:
                return WeatherStatusCodes.freezing_drizzle
            case [61, 63, 65]:
                return WeatherStatusCodes.rain
            case [66, 67]:
                return WeatherStatusCodes.freezing_rain
            case [71, 73, 75]:
                return WeatherStatusCodes.snow
            case 77:
                return WeatherStatusCodes.snow_grains
            case [80, 81, 82]:
                return WeatherStatusCodes.rain_showers
            case [85, 86]:
                return WeatherStatusCodes.snow_showers
            case [95, 96, 99]:
                return WeatherStatusCodes.thunderstorm
            case _:
                return WeatherStatusCodes.no_data

    def __init__(self):
        raise NotImplementedError(
            'You don\'t need to make an instance object. Just relate to existing fields and methods'
        )
