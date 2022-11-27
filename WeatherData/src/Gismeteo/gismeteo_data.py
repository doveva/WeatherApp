from ..weather_service import WeatherBaseService
from ..Utils.coordinates import Place


class GismeteoService(WeatherBaseService):
    def get_day_data(self, coords: Place) -> dict:
        pass

