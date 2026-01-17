import pytest


def test_lawnglass(lawnglass):
    assert lawnglass.name == "Газонная трава"
    assert lawnglass.description == "Элитная трава для газона"
    assert lawnglass.price == 500.0
    assert lawnglass.quantity == 20
    assert lawnglass.country == "Россия"
    assert lawnglass.germination_period == "7 дней"
    assert lawnglass.color == "Зеленый"


def test_lawnglass_add(lawnglass, lawnglass_2):
    assert lawnglass + lawnglass_2 == 17200.0


def test_lawnglass_add_error(lawnglass, lawnglass_2):
    with pytest.raises(TypeError):
        result = lawnglass + 1  # noqa: F841
