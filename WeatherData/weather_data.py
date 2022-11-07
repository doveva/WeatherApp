from abc import abstractmethod


class WeatherBase:
    """
    Базовый интерфейс для получения данных от источника
    """
    @abstractmethod
    def get_data(self) -> dict:
        pass
