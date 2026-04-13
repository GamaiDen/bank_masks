"""
Модуль для настройки логгеров.
"""
import logging
import sys
from pathlib import Path


def setup_logger(
    name: str,
    log_file: str,
    level: int = logging.DEBUG,
    console: bool = False
) -> logging.Logger:
    """
    Настраивает и возвращает логгер с заданным именем.

    Аргументы:
        name (str): Имя логгера (обычно __name__ модуля)
        log_file (str): Путь к файлу для записи логов
        level (int): Уровень логирования (по умолчанию DEBUG)
        console (bool): Выводить ли логи в консоль

    Возвращает:
        logging.Logger: Настроенный логгер
    """
    # Создаем директорию для логов, если её нет
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Очищаем существующие обработчики, чтобы не дублировать
    if logger.hasHandlers():
        logger.handlers.clear()

    # Создаем файловый обработчик
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(level)

    # Создаем форматтер
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Добавляем консольный обработчик, если нужно
    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
