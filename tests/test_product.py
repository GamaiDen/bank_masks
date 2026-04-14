"""
Тесты для класса Product.
"""

from src.product import Product


def test_product_initialization():
    """Тест корректной инициализации объекта Product."""
    product = Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_initialization_with_zero_quantity():
    """Тест инициализации с нулевым количеством."""
    product = Product(
        name="iPhone 15 Pro",
        description="128GB, Natural Titanium",
        price=150000.0,
        quantity=0
    )

    assert product.quantity == 0


def test_product_initialization_with_float_price():
    """Тест инициализации с дробной ценой."""
    product = Product(
        name="Xiaomi 14",
        description="512GB, Black",
        price=89999.99,
        quantity=3
    )

    assert product.price == 89999.99


def test_product_repr():
    """Тест строкового представления продукта."""
    product = Product(
        name="Test Product",
        description="Test Description",
        price=100.0,
        quantity=2
    )

    expected_repr = "Product(name='Test Product', price=100.0, quantity=2)"
    assert repr(product) == expected_repr
