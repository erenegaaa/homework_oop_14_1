from abc import ABC, abstractmethod


class BaseClass(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, **kwargs):  # Переопределение базового класса
        pass
