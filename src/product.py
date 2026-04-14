"""
Модуль для работы с продуктами.
"""


class Product:
    """
    Класс для представления продукта.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        price (float): Цена продукта.
        quantity (int): Количество в наличии.
    """

    name: str
    description: str
    price: float
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
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        """Строковое представление продукта."""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
