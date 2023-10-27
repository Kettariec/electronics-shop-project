import csv
import os


class InstantiateCSVError(Exception):
    """
    Класс-исключение
    """
    def __init__(self):
        self.message = "_Файл item.csv поврежден_"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    data = os.path.join('..', 'src', 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"('{self.__name}', {self.price}, {self.quantity})")

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return other.quantity + self.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создаём экземпляры класса Item данными из файла src/items.csv
        Добавляем экземпляры в список Item.all
        """
        try:
            cls.all.clear()
            with open(Item.data, 'r', encoding='windows-1251') as f:
                doc = csv.DictReader(f)
                items = []
                for i in doc:
                    if len(i) < 3:
                        raise InstantiateCSVError
                    name = i['name']
                    price = float(i['price'])
                    quantity = int(i['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)
                cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError("_Отсутствует файл item.csv_")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    @staticmethod
    def string_to_number(number) -> int:
        return int(float(number))
