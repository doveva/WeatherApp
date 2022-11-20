CREATE SCHEMA IF NOT EXISTS weather;

CREATE TABLE IF NOT EXISTS weather.gismeteo (
    id uuid PRIMARY KEY,
    weather int NOT NULL,
    humidity float NOT NULL,
    wind_dir text NOT NULL,
    wind_speed text NOT NULL ,
    date timestamp with time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS weather.points (
    id uuid PRIMARY KEY,
    name text NOT NULL,
    altitude float NOT NULL,
    longitude float NOT NULL
);

CREATE TABLE IF NOT EXISTS weather.openweather (
    id uuid PRIMARY KEY,
    weather int NOT NULL,
    humidity float NOT NULL,
    wind_dir text NOT NULL,
    wind_speed text NOT NULL ,
    date timestamp with time zone NOT NULL,
    point uuid REFERENCES weather.points(id) ON DELETE CASCADE
);
