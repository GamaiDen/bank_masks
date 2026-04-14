"""
Модуль для подсчета количества операций по категориям.
"""

from collections import Counter
from typing import Any, Dict, List


def count_by_categories(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой заданной категории.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о транзакциях.
        categories (List[str]): Список названий категорий для подсчета.

    Возвращает:
        Dict[str, int]: Словарь, где ключи — названия категорий, значения — количество операций.
    """
    result: Dict[str, int] = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "")
        if not isinstance(description, str):
            continue

        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1
                break

    return result


def count_by_categories_counter(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой заданной категории с использованием Counter.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о транзакциях.
        categories (List[str]): Список названий категорий для подсчета.

    Возвращает:
        Dict[str, int]: Словарь, где ключи — названия категорий, значения — количество операций.
    """
    category_counts: Counter = Counter()

    for transaction in transactions:
        description = transaction.get("description", "")
        if not isinstance(description, str):
            continue

        description_lower = description.lower()
        for category in categories:
            if category.lower() in description_lower:
                category_counts[category] += 1
                break

    return {category: category_counts.get(category, 0) for category in categories}
