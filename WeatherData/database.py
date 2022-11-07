from abc import abstractmethod


class BaseStorage:
    """
    Базовый класс для хранения данных
    """
    @abstractmethod
    def load_data(self, data: dict) -> None:
        pass
