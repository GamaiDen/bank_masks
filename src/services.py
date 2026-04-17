"""
Модуль с сервисами для обработки транзакций.
"""

import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def simple_search(transactions: List[Dict[str, Any]], query: str) -> str:
    """
    Простой поиск — возвращает JSON со всеми транзакциями,
    содержащими запрос в описании или категории.

    Args:
        transactions: Список словарей с транзакциями.
        query: Строка для поиска.

    Returns:
        JSON-строка с найденными транзакциями.
    """
    if not query:
        return json.dumps([], ensure_ascii=False)

    query_lower = query.lower()
    result = []

    for t in transactions:
        description = str(t.get("Описание", "")).lower()
        category = str(t.get("Категория", "")).lower()

        if query_lower in description or query_lower in category:
            result.append(t)

    logger.info(f"Поиск по '{query}': найдено {len(result)} транзакций")
    return json.dumps(result, ensure_ascii=False, indent=2)
