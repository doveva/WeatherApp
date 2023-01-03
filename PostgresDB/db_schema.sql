CREATE SCHEMA IF NOT EXISTS weather;

CREATE TABLE IF NOT EXISTS weather.places (
    id uuid default gen_random_uuid() PRIMARY KEY NOT NULL,
    name text NOT NULL,
    latitude float NOT NULL,
    longitude float NOT NULL
);

CREATE TABLE IF NOT EXISTS weather.openweather (
    id uuid PRIMARY KEY,
    dewpoint float NOT NULL,
    weather text NOT NULL,
    cloud_cover int NOT NULL,
    wind_speed_low float NOT NULL,
    wind_direction_low int,
    wind_speed_high float NOT NULL,
    wind_direction_high int,
    date timestamp NOT NULL,
    place uuid REFERENCES weather.places(id) ON DELETE CASCADE,
    created timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS weather.gismeteo (
    id uuid PRIMARY KEY,
    weather text NOT NULL,
    cloud_cover int NOT NULL,
    humidity float NOT NULL,
    wind_dir text NOT NULL,
    wind_speed text NOT NULL,
    date timestamp with time zone NOT NULL,
    place uuid REFERENCES weather.places(id) ON DELETE CASCADE,
    created timestamp NOT NULL
);

