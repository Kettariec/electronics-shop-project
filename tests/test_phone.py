from src.phone import Phone
import pytest


@pytest.fixture
def phone() -> Phone:
    return Phone("iPhone 14", 120000, 5, 2)


def test_item_initialized(phone) -> None:
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.sim == 2


def test_str(phone):
    assert str(phone) == "iPhone 14"


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_calculate_total_price(phone) -> None:
    assert phone.calculate_total_price() == 600000


def test_apply_discount(phone) -> None:
    phone.pay_rate = 0.8
    phone.apply_discount()
    assert phone.price == 96000


def test_name_setter():
    phone.name = 'test'
    assert phone.name == 'test'


def test_string_to_number():
    assert Phone.string_to_number('7.0') == 7


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_add(phone):
    phone2 = Phone("Sony Xperia", 50000, 2, 1)
    assert phone + phone2 == 7
    assert phone + 3 is None
