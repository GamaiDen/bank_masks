"""
Модуль для работы с категориями товаров.
"""

from typing import List

from src.product import Product


class Category:
    """
    Класс для представления категории товаров.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        __products (List[Product]): Приватный список товаров в категории.

    Атрибуты класса:
        category_count (int): Общее количество категорий.
        product_count (int): Общее количество товаров во всех категориях.
    """

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: List[Product]

    def __init__(self, name: str, description: str, products: List[Product] = None) -> None:
        """
        Инициализация объекта Category.

        Аргументы:
            name (str): Название категории.
            description (str): Описание категории.
            products (List[Product], optional): Список товаров в категории.
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.

        Аргументы:
            product (Product): Объект продукта для добавления.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для приватного атрибута __products.

        Возвращает:
            str: Строка с информацией о всех продуктах в категории.
        """
        if not self.__products:
            return ""

        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def get_products_list(self) -> List[Product]:
        """
        Возвращает список продуктов (для тестов и внутреннего использования).

        Возвращает:
            List[Product]: Список объектов Product.
        """
        return self.__products

    def __repr__(self) -> str:
        """Строковое представление категории."""
        return f"Category(name='{self.name}', products_count={len(self.__products)})"
