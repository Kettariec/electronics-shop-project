import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

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
    def instantiate_from_csv(cls, csv_doc):
        """
        Создаём экземпляры класса Item данными из файла src/items.csv
        Добавляем экземпляры в список Item.all
        """
        cls.all.clear()
        with open(csv_doc, 'r', encoding='windows-1251') as f:
            doc = csv.DictReader(f)
            items = []
            for i in doc:
                name = i['name']
                price = float(i['price'])
                quantity = int(i['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all = items

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    @staticmethod
    def string_to_number(number) -> int:
        return int(float(number))
