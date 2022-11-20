from ..weather_service import WeatherBaseService
from ..Utils.coordinates import Coordinates


class GismeteoService(WeatherBaseService):
    def get_day_data(self, coords: Coordinates) -> dict:
        pass

