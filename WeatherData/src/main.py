import json
from datetime import date, timedelta, datetime
from typing import List, Tuple
from kafka import KafkaProducer

from Utils.coordinates import Place
from Utils.datetime_range import DateRange

from OpenMeteo.open_meteo_model import spb_timezone
from OpenMeteo.open_meteo import OpenMeteoService

from weather_service import WeatherBaseService

from Places.places import PlacesDB


class WeatherETL:
    def __init__(self, coords_range: List[Place], services_list: Tuple[WeatherBaseService], kafka_host: list):
        start_date = date.today()
        end_date = start_date + timedelta(days=7)
        self._date_range = DateRange(start_date=start_date, end_date=end_date)
        self._coords = coords_range

        self._services = services_list

        self._producer = KafkaProducer(
            bootstrap_servers=kafka_host,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=str.encode,
            compression_type='gzip'
        )

    def send_data(self, service: WeatherBaseService):
        for coord in self._coords:
            data = service.get_period_json_data(coords=coord, date_range=self._date_range)
            result_data = {
                'Place': coord.id,
                'Data': data,
                'Created': datetime.now().replace(tzinfo=spb_timezone).replace(microsecond=0).isoformat()
            }
            self._producer.send('Weather', key=str(service), value=result_data)

    def run_etl(self):
        for service in self._services:
            self.send_data(service)


if __name__ == "__main__":
    WeatherETL(
        coords_range=PlacesDB().get_all_places(),
        services_list=(OpenMeteoService(),),
        kafka_host=['localhost:29093']
    ).run_etl()
