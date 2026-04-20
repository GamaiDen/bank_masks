from src.oop.base_product import BaseProduct

"""
Модуль для работы с продуктами.
"""

from src.oop.mixins import LogMixin


class Product(LogMixin, BaseProduct):
    """
    Класс для представления продукта.
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Класс-метод для создания продукта из словаря."""
        return cls(
            name=product_data.get("name", ""),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0),
        )

    @property
    def price(self) -> float:
        """Геттер цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Строковое представление."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: BaseProduct) -> float:
        """Сложение продуктов."""
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        return self.__price * self.quantity + other.__price * other.quantity


class Smartphone(Product):
    """Класс для смартфона."""

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
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: BaseProduct) -> float:
        if type(other) is not Smartphone:
            raise TypeError("Складывать можно только объекты класса Smartphone")
        return super().__add__(other)


class LawnGrass(Product):
    """Класс для газонной травы."""

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
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: BaseProduct) -> float:
        if type(other) is not LawnGrass:
            raise TypeError("Складывать можно только объекты класса LawnGrass")
        return super().__add__(other)
