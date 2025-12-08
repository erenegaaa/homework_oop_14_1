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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        """Добавление продукта в список и счетчик"""
        self.product_count += 1
        self.products.append(product)
