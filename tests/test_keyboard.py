from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard() -> Keyboard:
    return Keyboard('Dark Project Ultra', 12500, 3)


def test_item_initialized(keyboard) -> None:
    assert keyboard.name == "Dark Project Ultra"
    assert keyboard.price == 12500
    assert keyboard.quantity == 3


def test_str(keyboard):
    assert str(keyboard) == "Dark Project Ultra"


def test_repr(keyboard):
    assert repr(keyboard) == "Keyboard('Dark Project Ultra', 12500, 3)"


def test_calculate_total_price(keyboard) -> None:
    assert keyboard.calculate_total_price() == 37500


def test_apply_discount(keyboard) -> None:
    keyboard.pay_rate = 0.8
    keyboard.apply_discount()
    assert keyboard.price == 10000


def test_name_setter():
    keyboard.name = 'test'
    assert keyboard.name == 'test'


def test_string_to_number():
    assert Keyboard.string_to_number('9.0') == 9


def test_add(keyboard):
    keyboard2 = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard + keyboard2 == 8
    assert keyboard + 3 is None


def test_language(keyboard):
    assert keyboard.language == 'EN'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
