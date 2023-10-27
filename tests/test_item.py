from src.item import InstantiateCSVError
from src.item import Item
import pytest
import os


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


def test_add(item):
    item2 = Item("Планшет", 15000, 4)
    assert item + item2 == 6
    assert item + 5 is None


def test_file_not_found():
    Item.data = os.path.join('src', 'error.csv')
    with pytest.raises(FileNotFoundError, match='_Отсутствует файл item.csv_'):
        Item.instantiate_from_csv()


def test_instantiate_csv():
    Item.data = os.path.join('test.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
