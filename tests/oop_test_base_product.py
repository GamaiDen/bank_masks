"""
Тесты для абстрактного класса BaseProduct.
"""

import pytest
from src.oop.base_product import BaseProduct
from src.oop.product import Product


def test_product_is_subclass_of_base_product():
    """Продукт должен быть наследником BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_cannot_instantiate_base_product():
    """Нельзя создать экземпляр абстрактного класса."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 1)
