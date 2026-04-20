"""
Модуль для работы с JSON-файлами.
"""
import json
import logging
from pathlib import Path
<<<<<<< HEAD
from typing import List, Dict, Any
=======
from typing import Any, Dict, List
>>>>>>> a0698861399be6f9e192f762298ffe8731c117df

from src.loggers.setup_logger import setup_logger

# Настройка логгера для модуля utils
logger = setup_logger(
    name=__name__,
    log_file="logs/utils.log",
    level=logging.DEBUG
)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.

    Аргументы:
        file_path (str): Путь к JSON-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список транзакций.
        Если файл пустой, содержит не список или не найден - возвращает пустой список.
    """
    logger.debug(f"Начало чтения файла: {file_path}")
    path = Path(file_path)

    if not path.is_file():
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        logger.debug(f"Файл успешно прочитан: {file_path}")
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}. Файл: {file_path}")
        return []
    except OSError as e:
        logger.error(f"Ошибка доступа к файлу: {e}. Файл: {file_path}")
        return []

    if isinstance(data, list):
        logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
        return data
    else:
        logger.error(f"Файл {file_path} содержит не список, а {type(data).__name__}")
        return []
