class Product:
    """Класс продуктов."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Возвращает имя товара, цену и количество в строковом формате"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"


    @property
    def price(self):
        """Возвращение цены"""
        return self.__price


    @classmethod
    def new_product(cls, product_data):
        """Добавление нового товара с условием дублирования"""
        return cls(
            name = product_data["name"],
            description = product_data["description"],
            price = product_data["price"],
            quantity = product_data["quantity"]
        )


    @price.setter
    def price(self, value):
        """Возвращаем цену если она не ровна нулю или не является отрицательной"""
        if value <= 0:
            print("""Цена не должна быть нулевая или отрицательная""")
            return
        self.__price = value


    def __add__(self, other):
        """
        Метод позволяющий сложить цену и количество продуктов
        Вид формулы: a * b + a * b
        """
        return self.price * self.quantity + other.price * other.quantity