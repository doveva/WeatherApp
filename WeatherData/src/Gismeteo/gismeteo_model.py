from Models.base_model import BaseMeteoModel

from Utils.status_codes import WeatherStatusCodes

from datetime import datetime


class GismeteoModel(BaseMeteoModel):
    Humidity: int
    Weather: str
    CloudCover: int
    WindSpeed: float
    WindDirection: int = None
    Datetime: datetime

    @classmethod
    def create_model(cls, data: dict) -> BaseMeteoModel:
        result = {}
        try:
            result['Humidity'] = data['humidity']['percent']
            result['Weather'] = GismeteoMapper.weather_code(
                data['cloudiness']['type'],
                data['precipitation']['type'],
                data['precipitation']['intensity']
            )
            result['CloudCover'] = data['cloudiness']['percent']
            result['WindSpeed'] = data['wind']['speed']['m_s']
            result['WindDirection'] = data['wind']['direction']['degree']
            result['Datetime'] = datetime.strptime(data['date']['local'], '%Y-%m-%d %H:%M:%S')
        except KeyError:
            print('Some data was not provided!')
        return cls(**result)


class GismeteoMapper:
    @classmethod
    def weather_code(
            cls,
            weather_code: int,
            precipitation: int,
            intensity: int,
    ) -> str:
        def precipitation_find(precipitation_code: int, intensity_code: int) -> str:
            match precipitation_code:
                case 1:
                    match intensity_code:
                        case 1 | 2:
                            return WeatherStatusCodes.rain
                        case 3:
                            return WeatherStatusCodes.rain_showers
                case 2 | 3:
                    match intensity_code:
                        case 1:
                            return WeatherStatusCodes.snow_grains
                        case 2:
                            return WeatherStatusCodes.snow
                        case 3:
                            return WeatherStatusCodes.snow_showers

        match weather_code:
            case 0:
                return WeatherStatusCodes.clear
            case 1 | 101:
                return WeatherStatusCodes.mainly_clear
            case 2:
                match precipitation:
                    case 0:
                        return WeatherStatusCodes.partly_cloudy
                    case _:
                        return precipitation_find(
                            precipitation_code=precipitation,
                            intensity_code=intensity
                        )
            case 3:
                match precipitation:
                    case 0:
                        return WeatherStatusCodes.overcast
                    case _:
                        return precipitation_find(
                            precipitation_code=precipitation,
                            intensity_code=intensity
                        )
