"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_class_item():
    res = Item("Смартфон", 10000, 20)
    assert res.calculate_total_price() == 200000



