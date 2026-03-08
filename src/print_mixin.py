class PrintMixin:
    """Выводит информацию о продукте в терминал"""
    def __init__(self):
        print(repr(self))




    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"