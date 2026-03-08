from src.products import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_print_mixin(capsys):
    Product("Nokia 3310", "Агрегат для всего", 850, 3)
    message = capsys.readouterr()
    assert message.out.strip() == "Product, Nokia 3310, 850 руб. Остаток: 3 шт."

    Smartphone("Samsung Galaxy S23 Ultra",
               "256GB, Серый цвет, 200MP камера",
               180000.0,
               5,
               95.5,
               "S23 Ultra",
               256,
               "Серый"
               )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone, Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

    LawnGrass("Газонная трава",
              "Элитная трава для газона",
              500.0,
              20,
              "Россия",
              "7 дней",
              "Зеленый"
              )
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass, Газонная трава, 500.0 руб. Остаток: 20 шт."


