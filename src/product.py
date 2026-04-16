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

    def __repr__(self) -> str:
        """Строковое представление продукта."""
        return f"Product(name='{self.name}', price={self.__price}, quantity={self.quantity})"
