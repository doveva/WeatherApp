from abc import abstractmethod
from pydantic import BaseModel


class BaseStorage:
    """
    Базовый класс для хранения данных
    """
    @abstractmethod
    def load_data(self, data: BaseModel) -> None:
        pass
