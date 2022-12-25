from sqlalchemy.engine import create_engine, URL
from sqlalchemy.sql import select
from sqlalchemy import Table, Column, String, Float, MetaData
from sqlalchemy.dialects.postgresql import UUID

from Core.settings import config
from Utils.coordinates import Place


class PlacesDB:
    def __init__(self):
        url = URL.create(
            drivername='postgresql+psycopg2',
            database=config.POSTGRES_DB,
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
            username=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD
        )
        engine = create_engine(url=url)
        self.conn = engine.connect()
        self.places = Table(
            'places',
            MetaData(schema='weather'),
            Column('id', UUID(as_uuid=False), primary_key=True),
            Column('name', String),
            Column('latitude', Float),
            Column('longitude', Float),
        )

    def get_all_places(self) -> list[Place]:
        places = self.conn.execute(select(self.places))
        result = []
        for place in places:
            result.append(Place(
                **{
                    'id': place[0],
                    'name': place[1],
                    'latitude': place[2],
                    'longitude': place[3]
                }
            ))
        return result
