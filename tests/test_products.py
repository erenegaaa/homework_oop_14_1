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


def test_price_is_not_zero_or_negative():
    """Тест на отрицательную цену или равную нулю"""
    with pytest.raises(ValueError):
        Product("lg", "44d", 0, 1)
    with pytest.raises(ValueError):
        Product("nokia", "3310", -100, 1)
