<<<<<<< HEAD
=======
from src.oop.base_product import BaseProduct

>>>>>>> 867fa72 (style: fix isort and flake8 issues)
"""
Модуль для работы с продуктами.
"""


class Product:
    """
    Класс для представления продукта.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        __price (float): Цена продукта (приватный).
        quantity (int): Количество в наличии.
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта Product.

        Аргументы:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество в наличии.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """
        Класс-метод для создания объекта Product из словаря.

        Аргументы:
            product_data (dict): Словарь с данными продукта.

        Возвращает:
            Product: Экземпляр класса Product.
        """
        return cls(
            name=product_data.get("name", ""),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0),
        )

    @property
    def price(self) -> float:
        """
        Геттер для приватного атрибута __price.

        Возвращает:
            float: Цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для приватного атрибута __price.

        Аргументы:
            new_price (float): Новая цена продукта.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """
        Строковое представление продукта.

        Возвращает:
            str: Строка в формате "Название, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Магический метод сложения двух продуктов.

        Аргументы:
            other (Product): Другой продукт.

        Возвращает:
            float: Сумма произведений цены на количество для двух продуктов.
        """
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        return self.__price * self.quantity + other.__price * other.quantity

    def __repr__(self) -> str:
        """Строковое представление продукта для отладки."""
        return f"Product(name='{self.name}', price={self.__price}, quantity={self.quantity})"


class Smartphone(Product):
    """
    Класс для представления смартфона, наследник Product.

    Дополнительные атрибуты:
        efficiency (float): Производительность.
        model (str): Модель.
        memory (int): Объем встроенной памяти.
        color (str): Цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализация объекта Smartphone."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Product") -> float:
        """
        Сложение смартфонов. Разрешено только с объектами Smartphone.
        """
        if type(other) is not Smartphone:
            raise TypeError("Складывать можно только объекты класса Smartphone")
        return super().__add__(other)


class LawnGrass(Product):
    """
    Класс для представления газонной травы, наследник Product.

    Дополнительные атрибуты:
        country (str): Страна-производитель.
        germination_period (int): Срок прорастания (дней).
        color (str): Цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        """Инициализация объекта LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "Product") -> float:
        """
        Сложение газонной травы. Разрешено только с объектами LawnGrass.
        """
        if type(other) is not LawnGrass:
            raise TypeError("Складывать можно только объекты класса LawnGrass")
        return super().__add__(other)
