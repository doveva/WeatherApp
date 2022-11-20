from src.Utils.coordinates import Coordinates
from src.Utils.datetime_range import DateRange

from src.OpenMeteo.open_meteo import OpenMeteoService
from datetime import date, timedelta
from typing import List


class WeatherETL:
    def __init__(self, coords_range: List[Coordinates]):
        start_date = date.today()
        end_date = start_date + timedelta(days=7)
        self._date_range = DateRange(start_date=start_date, end_date=end_date)
        self._coords = coords_range

    def run_etl(self):
        for coord in self._coords:
            OpenMeteoService().get_period_data(coords=coord, date_range=self._date_range)


if __name__ == "__main__":
    WeatherETL(coords_range=[Coordinates(latitude=59.93, longitude=30.31)]).run_etl()
