from src.products import Product


class Smartphone(Product):
    """Категория товаров (Смартфон)"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)  # передаем аргументы базового класса !!!
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Невозможно складывать продукты разных категорий")
