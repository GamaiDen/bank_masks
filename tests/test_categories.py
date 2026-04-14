"""
Тесты для модуля categories.
"""

import pytest
from src.categories import count_by_categories, count_by_categories_counter


def test_count_by_categories_empty():
    """Пустой список транзакций возвращает нули."""
    result = count_by_categories([], ["Перевод", "Оплата"])
    assert result == {"Перевод": 0, "Оплата": 0}


def test_count_by_categories_single_match():
    """Одна транзакция попадает в одну категорию."""
    transactions = [{"description": "Перевод с карты на карту"}]
    result = count_by_categories(transactions, ["Перевод", "Оплата"])
    assert result == {"Перевод": 1, "Оплата": 0}


def test_count_by_categories_multiple_matches():
    """Несколько транзакций в разных категориях."""
    transactions = [
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата услуг связи"},
        {"description": "Перевод организации"},
        {"description": "Оплата интернета"},
    ]
    result = count_by_categories(transactions, ["Перевод", "Оплата"])
    assert result == {"Перевод": 2, "Оплата": 2}


def test_count_by_categories_case_insensitive():
    """Подсчет нечувствителен к регистру."""
    transactions = [
        {"description": "ПЕРЕВОД"},
        {"description": "перевод"},
    ]
    result = count_by_categories(transactions, ["Перевод"])
    assert result == {"Перевод": 2}


def test_count_by_categories_missing_description():
    """Транзакции без description игнорируются."""
    transactions = [{"amount": 100}, {"description": "Перевод"}]
    result = count_by_categories(transactions, ["Перевод"])
    assert result == {"Перевод": 1}


def test_count_by_categories_counter():
    """Тест функции с Counter."""
    transactions = [
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата услуг связи"},
        {"description": "Перевод организации"},
    ]
    result = count_by_categories_counter(transactions, ["Перевод", "Оплата"])
    assert result == {"Перевод": 2, "Оплата": 1}
