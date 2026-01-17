import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


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


@pytest.fixture(autouse=True)
def reset_counters():
    Category.product_count = 0
    Category.category_count = 0


@pytest.fixture
def empty_category():
    return Category("Phones", "desc", [])


@pytest.fixture
def smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      256,
                      "Серый"
                      )


@pytest.fixture
def smartphone_2():
    return Smartphone("Samsung Galaxy S21 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      97000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      512,
                      "black"
                      )


@pytest.fixture
def lawnglass():
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0,
                     20,
                     "Россия",
                     "7 дней",
                     "Зеленый"
                     )


@pytest.fixture
def lawnglass_2():
    return LawnGrass("Газонная трава",
                     "Трава для газона",
                     360.0,
                     20,
                     "Россия",
                     "14 дней",
                     "Зеленый"
                     )
