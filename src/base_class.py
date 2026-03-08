from abc import ABC, abstractmethod


class BaseClass(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, **product_data):  # Переопределение базового класса
        pass
