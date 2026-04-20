import pytest

from src.oop.product import LawnGrass, Product, Smartphone

"""
Тесты для класса Product.
"""


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


def test_product_price_getter():
    """Тест геттера цены."""
    product = Product("Test", "Desc", 100.0, 1)
    assert product.price == 100.0


def test_product_price_setter_valid():
    """Тест сеттера цены с корректным значением."""
    product = Product("Test", "Desc", 100.0, 1)
    product.price = 200.0
    assert product.price == 200.0


def test_product_price_setter_invalid(capsys):
    """Тест сеттера цены с некорректным значением."""
    product = Product("Test", "Desc", 100.0, 1)
    product.price = -50.0
    captured = capsys.readouterr()
    assert product.price == 100.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_setter_zero(capsys):
    """Тест сеттера цены с нулевым значением."""
    product = Product("Test", "Desc", 100.0, 1)
    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 100.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_classmethod():
    """Тест класс-метода new_product."""
    product_data = {
        "name": "iPhone 15",
        "description": "128GB",
        "price": 99999.99,
        "quantity": 3
    }
    product = Product.new_product(product_data)

    assert product.name == "iPhone 15"
    assert product.description == "128GB"
    assert product.price == 99999.99
    assert product.quantity == 3


def test_product_repr():
    """Тест строкового представления продукта."""
    product = Product("Test", "Desc", 100.0, 2)
    assert 'Product' in repr(product)


def test_product_str():
    """Тест строкового представления продукта."""
    product = Product("Samsung", "Phone", 80000.0, 3)
    assert str(product) == "Samsung, 80000.0 руб. Остаток: 3 шт."


def test_product_add():
    """Тест магического метода сложения продуктов."""
    p1 = Product("Товар 1", "Описание", 100.0, 10)
    p2 = Product("Товар 2", "Описание", 200.0, 2)
    result = p1 + p2
    assert result == 1400.0  # 100*10 + 200*2


def test_product_add_type_error():
    """Тест ошибки при сложении с не-продуктом."""
    p1 = Product("Товар", "Описание", 100.0, 1)
    with pytest.raises(TypeError):
        _ = p1 + "не продукт"


def test_smartphone_init():
    """Тест инициализации смартфона."""
    phone = Smartphone(
        "iPhone 15", "Смартфон", 100000.0, 2, 9.8, "15 Pro", 256, "Black"
    )
    assert phone.name == "iPhone 15"
    assert phone.efficiency == 9.8
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"


def test_lawn_grass_init():
    """Тест инициализации газонной травы."""
    grass = LawnGrass(
        "Green Grass", "Трава", 500.0, 10, "Россия", 14, "Зеленый"
    )
    assert grass.name == "Green Grass"
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Зеленый"


def test_smartphone_add_same_class():
    """Тест сложения двух смартфонов."""
    phone1 = Smartphone("A", "", 100.0, 2, 1.0, "M1", 64, "Red")
    phone2 = Smartphone("B", "", 200.0, 1, 2.0, "M2", 128, "Blue")
    assert phone1 + phone2 == 400.0


def test_smartphone_add_different_class():
    """Тест сложения смартфона с другим классом."""
    phone = Smartphone("A", "", 100.0, 1, 1.0, "M", 64, "Red")
    grass = LawnGrass("B", "", 50.0, 2, "RU", 7, "Green")
    with pytest.raises(TypeError):
        _ = phone + grass


def test_lawn_grass_add_same_class():
    """Тест сложения двух упаковок травы."""
    grass1 = LawnGrass("A", "", 100.0, 3, "RU", 7, "Green")
    grass2 = LawnGrass("B", "", 200.0, 1, "USA", 10, "Dark Green")
    assert grass1 + grass2 == 500.0
