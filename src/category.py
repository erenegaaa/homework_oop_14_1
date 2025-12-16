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
        self.__products = list(products) if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

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
        return self.__products
