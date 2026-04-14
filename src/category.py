"""
Модуль для работы с категориями товаров.
"""

from typing import List, Optional
from src.product import Product


class Category:
    """
    Класс для представления категории товаров.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        products (List[Product]): Список товаров в категории.

    Атрибуты класса:
        category_count (int): Общее количество категорий.
        product_count (int): Общее количество товаров во всех категориях.
    """

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: List[Product]

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализация объекта Category.

        Аргументы:
            name (str): Название категории.
            description (str): Описание категории.
            products (Optional[List[Product]]): Список товаров в категории.
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __repr__(self) -> str:
        """Строковое представление категории."""
        return f"Category(name='{self.name}', products_count={len(self.products)})"
