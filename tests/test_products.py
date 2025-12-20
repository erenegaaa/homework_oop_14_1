import pytest
from src.products import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания объекта продукта."""
    return Product(
        name="Nokia 3310",
        description="Агрегат для всего",
        price=850,
        quantity=3
    )


@pytest.fixture
def sample_product_2():
    """Фикстура для создания объекта продукта."""
    return Product(
        name="iphone",
        description="512/12",
        price=399000,
        quantity=3
    )


def test_product_attibutes(sample_product):
    assert sample_product.name == "Nokia 3310"
    assert sample_product.description == "Агрегат для всего"
    assert sample_product.price == 850
    assert sample_product.quantity == 3


def test_product_types(sample_product):
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, int)
    assert isinstance(sample_product.quantity, int)


def test_price_is_not_zero_or_negative(capsys):
    product = Product("lg", "44d", 100, 1)

    product.price = 0
    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100

def test_str_product(sample_product):
    assert str(sample_product) == "Nokia 3310, 850 руб. Остаток: 3 шт.\n"


def test_add_products(sample_product, sample_product_2):
    assert sample_product + sample_product_2 == 1199550