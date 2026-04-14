"""
Тесты для класса Category.
"""

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми продуктами."""
    return [
        Product("Product 1", "Description 1", 100.0, 10),
        Product("Product 2", "Description 2", 200.0, 5),
        Product("Product 3", "Description 3", 300.0, 0),
    ]


def test_category_initialization_empty_products():
    """Тест инициализации категории без продуктов."""
    category = Category(
        name="Смартфоны",
        description="Категория смартфонов"
    )

    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert category.products == []


def test_category_initialization_with_products(sample_products):
    """Тест инициализации категории с продуктами."""
    category = Category(
        name="Тестовая категория",
        description="Описание тестовой категории",
        products=sample_products
    )

    assert category.name == "Тестовая категория"
    assert category.description == "Описание тестовой категории"
    assert len(category.products) == 3
    assert category.products[0].name == "Product 1"
    assert category.products[1].price == 200.0
    assert category.products[2].quantity == 0


def test_category_count_increment():
    """Тест увеличения счетчика категорий."""
    initial_count = Category.category_count

    Category("Категория 1", "Описание 1")
    Category("Категория 2", "Описание 2")
    Category("Категория 3", "Описание 3")

    assert Category.category_count == initial_count + 3


def test_product_count_increment(sample_products):
    """Тест увеличения счетчика продуктов."""
    initial_count = Category.product_count

    Category(
        name="Категория с продуктами",
        description="Описание",
        products=sample_products
    )

    assert Category.product_count == initial_count + 3


def test_product_count_with_empty_category():
    """Тест счетчика продуктов при создании пустой категории."""
    initial_count = Category.product_count

    Category("Пустая категория", "Без продуктов")

    assert Category.product_count == initial_count


def test_category_repr():
    """Тест строкового представления категории."""
    category = Category("Тест", "Описание")
    expected_repr = "Category(name='Тест', products_count=0)"
    assert repr(category) == expected_repr


def test_category_repr_with_products(sample_products):
    """Тест строкового представления категории с продуктами."""
    category = Category("Тест", "Описание", sample_products)
    expected_repr = "Category(name='Тест', products_count=3)"
    assert repr(category) == expected_repr
