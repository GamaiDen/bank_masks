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
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура с тестовой категорией."""
    return Category("Test Category", "Description", sample_products)


def test_category_initialization(sample_products):
    """Тест инициализации категории."""
    category = Category("Test", "Desc", sample_products)
    assert category.name == "Test"
    assert category.description == "Desc"
    assert len(category.get_products_list()) == 2


def test_add_product(sample_category, sample_products):
    """Тест добавления продукта в категорию."""
    initial_count = Category.product_count
    new_product = Product("Product 3", "Desc 3", 300.0, 2)

    sample_category.add_product(new_product)

    assert len(sample_category.get_products_list()) == 3
    assert Category.product_count == initial_count + 1


def test_products_getter(sample_category):
    """Тест геттера products."""
    products_str = sample_category.products

    assert "Product 1, 100.0 руб. Остаток: 10 шт." in products_str
    assert "Product 2, 200.0 руб. Остаток: 5 шт." in products_str


def test_products_getter_empty():
    """Тест геттера products для пустой категории."""
    category = Category("Empty", "Desc")
    assert category.products == ""


def test_category_count_increment():
    """Тест увеличения счетчика категорий."""
    initial = Category.category_count
    Category("Cat 1", "Desc")
    Category("Cat 2", "Desc")
    assert Category.category_count == initial + 2


def test_category_repr(sample_category):
    """Тест строкового представления категории."""
    assert repr(sample_category) == "Category(name='Test Category', products_count=2)"


def test_category_str(sample_category):
    """Тест строкового представления категории."""
    expected = "Test Category, количество продуктов: 15 шт."  # 10 + 5 из фикстуры
    assert str(sample_category) == expected
