CREATE SCHEMA IF NOT EXISTS weather;

CREATE TABLE IF NOT EXISTS weather.gismeteo (
    id uuid PRIMARY KEY,
    weather int NOT NULL,
    humidity float NOT NULL,
    wind_dir text NOT NULL,
    wind_speed text NOT NULL ,
    date timestamp with time zone NOT NULL
);