"""
Модуль для работы с JSON-файлами.
"""
import json
from pathlib import Path
from typing import Any, Dict, List


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.

    Аргументы:
        file_path (str): Путь к JSON-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список транзакций.
        Если файл пустой, содержит не список или не найден - возвращает пустой список.
    """
    path = Path(file_path)

    if not path.is_file():
        return []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    if isinstance(data, list):
        return data
    return []
