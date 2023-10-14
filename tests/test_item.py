from src.item import Item
import pytest


@pytest.fixture
def item() -> Item:
    return Item("Смартфон", 1000, 2)


def test_item_initialized(item) -> None:
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 1000, 2)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_calculate_total_price(item) -> None:
    assert item.calculate_total_price() == 2000


def test_apply_discount(item) -> None:
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 800


def test_name_setter():
    item.name = 'test2'
    assert item.name == 'test2'


def test_string_to_number():
    assert Item.string_to_number('5.0') == 5
