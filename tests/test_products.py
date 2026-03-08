from src.products import Product


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


def test_product_init(product):
    assert product.name == "Phone"
    assert product.description == "Smartphone"
    assert product.price == 1000
    assert product.quantity == 5


def test_product_str(product):
    assert str(product) == "Phone, 1000 руб. Остаток: 5 шт.\n"


def test_price_getter(product):
    assert product.price == 1000


def test_price_setter(product):
    product.price = 1500
    assert product.price == 1500


def test_price_setter_negative(product):
    product.price = -500
    assert product.price == 1000


def test_new_product(product):
    data = {
        "name": "Tablet",
        "description": "Android tablet",
        "price": 500,
        "quantity": 10
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Tablet"
    assert product.price == 500
    assert product.quantity == 10


def test_add_product(product, second_product):
    result = product + second_product
    assert result == 1000 * 5 + 2000 * 3
