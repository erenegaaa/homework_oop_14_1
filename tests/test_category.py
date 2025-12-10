import pytest
from src.category import Category
from src.products import Product


@pytest.fixture
def sample_category():
    return Category(
        name="Телефоны", description="От мобильных до стационарных",
        products=[
            Product(
                name="Vivo - blue Sky, 64Gb", description="Неплохой гаджет",
                price=13000, quantity=5
            )
        ]
    )


def test_category_attributes(sample_category):
    assert sample_category.name == "Телефоны"
    assert sample_category.description == "От мобильных до стационарных"
    assert sample_category.products[0].name == "Vivo - blue Sky, 64Gb"
    assert sample_category.products[0].description == "Неплохой гаджет"
    assert sample_category.products[0].price == 13000
    assert sample_category.products[0].quantity == 5


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
    assert empty_category.product_count == 0
    assert len(empty_category.products) == 0

    empty_category.add_product(sample_product)

    assert empty_category.product_count == 1
    assert empty_category.products[0] == sample_product
