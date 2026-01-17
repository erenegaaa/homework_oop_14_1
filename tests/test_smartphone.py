import pytest

def test_smartphone(smartphone):
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"

def test_smartphone_add(smartphone, smartphone_2):
    assert smartphone + smartphone_2 == 1385000.0


def test_smartphone_add_error(smartphone, smartphone_2):
    with pytest.raises(TypeError):
        result = smartphone + 1
