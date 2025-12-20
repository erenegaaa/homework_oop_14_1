import pytest
from src.category import Category
from src.products import Product


@pytest.fixture
def sample_category():
    return Category(
        name="Телефоны", description="От мобильных до стационарных",
        products=[
            Product(
                name="Vivo", description="Неплохой гаджет",
                price=13000, quantity=5
            )
        ]
    )


def test_category_attributes(sample_category):
        products_str = sample_category.products
        assert "Vivo, 13000 руб. Остаток: 5 шт.\n" in products_str


def test_category_types(sample_category):
    isinstance(sample_category.name, str)
    isinstance(sample_category.description, str)
    isinstance(sample_category.products[0], Product)


def test_category_counters():
    Category.category_count = 0
    Category.product_count = 0

    Category("Телефоны", "Описание", [
        Product("A", "desc", 100, 1),
        Product("B", "desc", 200, 2)
    ])

    Category("Ноутбуки", "Описание", [
        Product("C", "desc", 300, 1)
    ])

    assert Category.category_count == 2
    assert Category.product_count == 3


@pytest.fixture(autouse=True)
def reset_counters():
    Category.product_count = 0
    Category.category_count = 0


@pytest.fixture
def empty_category():
    return Category("Phones", "desc", [])


@pytest.fixture
def sample_product():
    return Product("iPhone", "desc", 100000, 5)


def test_add_product(empty_category, sample_product):
    assert Category.product_count == 0
    assert empty_category.products == ""

    empty_category.add_product(sample_product)

    assert Category.product_count == 1
    assert empty_category.products == (
        "iPhone, 100000 руб. Остаток: 5 шт.\n"
    )


def test_add_product_to_category():
    category = Category("Phones", "desc")
    product = Product("iPhone", "desc", 100000, 5)

    category.add_product(product)

    products_str = category.products

    assert products_str.count("\n") == 1
    assert "iPhone, 100000 руб. Остаток: 5 шт." in products_str



def test_add_duplicate_product():
    category = Category("Phones", "desc")
    product1 = Product("Vivo", "128/6", 17000, 3)
    product2 = Product("Vivo", "128/6", 19000, 3)

    category.add_product(product1)
    category.add_product(product2)

    products_str = category.products

    assert products_str.count("\n") == 1
    assert "Vivo, 19000 руб." in products_str
    assert "Остаток: 6 шт." in products_str


def test_category_str(sample_category):
    assert str(sample_category) == "Телефоны, количество продуктов: 5 шт."
