"""
Модуль для чтения финансовых транзакций из CSV и Excel файлов.
"""
from typing import Any, Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Аргументы:
        file_path (str): Путь к CSV-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список словарей с транзакциями.
        Если файл не найден или пуст, возвращает пустой список.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return []
        return df.to_dict(orient='records')
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    Аргументы:
        file_path (str): Путь к Excel-файлу (.xlsx).

    Возвращает:
        List[Dict[str, Any]]: Список словарей с транзакциями.
        Если файл не найден или пуст, возвращает пустой список.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        if df.empty:
            return []
        return df.to_dict(orient='records')
    except (FileNotFoundError, ValueError, Exception):
        return []
