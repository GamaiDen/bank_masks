"""
Модуль для поиска транзакций по описанию с использованием регулярных выражений.
"""

import re
from typing import Any, Dict, List


def search_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, в описании которых содержится указанная строка.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о транзакциях.
        search_string (str): Строка для поиска в поле 'description'.

    Возвращает:
        List[Dict[str, Any]]: Список словарей, у которых в описании найдена искомая строка.
    """
    if not search_string:
        return []

    result: List[Dict[str, Any]] = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    for transaction in transactions:
        description = transaction.get("description", "")
        if isinstance(description, str) and pattern.search(description):
            result.append(transaction)

    return result
