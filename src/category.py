class Category:
    """Класс категорий."""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1


        if products:
            for product in products:
                self.add_product(product)

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Добавление продукта в список, увеличивая счетчик с условием дублирования продуктов"""
        for existing_product in self.__products:
            if (
                existing_product.name == product.name
                and existing_product.description == product.description
                ):
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращение продуктов"""
        result = ""
        for product in self.__products:
            result += str(product)
        return result
