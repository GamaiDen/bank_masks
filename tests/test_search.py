"""
Тесты для модуля search.
"""

import pytest
from src.search import search_by_description


def test_search_by_description_empty_search_string():
    """Пустая строка поиска возвращает пустой список."""
    transactions = [{"description": "Перевод"}, {"description": "Оплата"}]
    result = search_by_description(transactions, "")
    assert result == []


def test_search_by_description_found():
    """Поиск находит совпадения."""
    transactions = [
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата услуг связи"},
        {"description": "Перевод организации"},
    ]
    result = search_by_description(transactions, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод с карты на карту"
    assert result[1]["description"] == "Перевод организации"


def test_search_by_description_not_found():
    """Поиск не находит совпадений."""
    transactions = [
        {"description": "Перевод с карты"},
        {"description": "Оплата услуг"},
    ]
    result = search_by_description(transactions, "зарплата")
    assert result == []


def test_search_by_description_case_insensitive():
    """Поиск нечувствителен к регистру."""
    transactions = [{"description": "ПЕРЕВОД"}, {"description": "перевод"}]
    result = search_by_description(transactions, "Перевод")
    assert len(result) == 2


def test_search_by_description_missing_field():
    """Транзакции без поля description игнорируются."""
    transactions = [{"amount": 100}, {"description": "Перевод"}]
    result = search_by_description(transactions, "перевод")
    assert len(result) == 1
