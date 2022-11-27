import json
from datetime import date, timedelta, datetime
from typing import List, Tuple
from kafka import KafkaProducer

from src.Utils.coordinates import Place
from src.Utils.datetime_range import DateRange

from src.OpenMeteo.open_meteo import OpenMeteoService

from src.weather_service import WeatherBaseService


class WeatherETL:
    def __init__(self, coords_range: List[Place], services_list: Tuple[WeatherBaseService], kafka_host: str):
        start_date = date.today()
        end_date = start_date + timedelta(days=7)
        self._date_range = DateRange(start_date=start_date, end_date=end_date)
        self._coords = coords_range

        self._services = services_list

        self._producer = KafkaProducer(
            bootstrap_servers=kafka_host,
            value_serializer=lambda v: json.dumps(v).encode('ascii'),
            key_serializer=str.encode,
            compression_type='gzip'
        )

    def send_data(self, service: WeatherBaseService):
        for coord in self._coords:
            data = service.get_period_json_data(coords=coord, date_range=self._date_range)
            result_data = {
                'place': coord.name,
                'data': data,
                'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self._producer.send('Weather', key=str(service), value=result_data)

    def run_etl(self):
        for service in self._services:
            self.send_data(service)


if __name__ == "__main__":
    WeatherETL(
        coords_range=[Place(name='Saint-Petersburg', latitude=59.93, longitude=30.31)],
        services_list=(OpenMeteoService(),),
        kafka_host='localhost:29092'
    ).run_etl()
