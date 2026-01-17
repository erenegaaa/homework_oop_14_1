from src.products import Product

class LawnGrass(Product):
    """Категория товара (трава газонная)"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity) # передаем аргументы базового класса!!!
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Невозможно складывать продукты разных категорий")