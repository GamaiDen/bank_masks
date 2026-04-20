"""
Тесты для миксина LogMixin.
"""

from src.oop.product import Product


def test_log_mixin_prints_on_creation(capsys):
    """При создании продукта выводится лог."""
    Product("Test", "Desc", 100.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out


def test_log_mixin_repr():
    """Проверка __repr__ от миксина."""
    p = Product("Test", "Desc", 100.0, 5)
    repr_str = repr(p)
    assert "Product" in repr_str
    assert "Test" in repr_str
    assert "100.0" in repr_str
    assert "5" in repr_str
