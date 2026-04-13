"""
Модуль для маскировки номеров карт и счетов.
"""
import logging
import re

from src.loggers.setup_logger import setup_logger

# Настройка логгера для модуля masks
logger = setup_logger(
    name=__name__,
    log_file="logs/masks.log",
    level=logging.DEBUG
)


def get_mask_card_number(card_number) -> str:
    """
    Маскирует номер банковской карты.

    Аргументы:
        card_number (str | int): Номер карты (16 цифр)

    Возвращает:
        str: Замаскированный номер карты в формате XXXX XX** **** XXXX
    """
    # Преобразуем в строку
    card_str = str(card_number)

    # Извлекаем только цифры
    digits = re.sub(r'\D', '', card_str)

    # Формируем сообщение для отладки
    preview = f"{digits[:4]}******{digits[-4:] if len(digits) > 4 else ''}"
    debug_msg = f"Маскировка номера карты: {preview}"
    logger.debug(debug_msg)

    # Если цифр меньше 16, возвращаем исходную строку (по ТЗ)
    if len(digits) != 16:
        logger.error(f"Номер карты должен содержать 16 цифр. Получено: {len(digits)}")
        return card_str

    try:
        masked = f"{digits[:4]} {digits[4:6]}** **** {digits[12:]}"
        logger.info(f"Карта успешно замаскирована: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {e}")
        return card_str


def get_mask_account(account_number) -> str:
    """
    Маскирует номер банковского счета.

    Аргументы:
        account_number (str | int): Номер счета

    Возвращает:
        str: Замаскированный номер счета в формате **XXXX
    """
    # Преобразуем в строку
    account_str = str(account_number)

    # Извлекаем только цифры
    digits = re.sub(r'\D', '', account_str)

    logger.debug(f"Маскировка номера счета: {account_str}")

    if not digits:
        logger.error("Пустой номер счета")
        return account_str

    if len(digits) < 4:
        logger.error(f"Номер счета слишком короткий: {digits}")
        return account_str

    try:
        masked = f"**{digits[-4:]}"
        logger.info(f"Счет успешно замаскирован: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке счета: {e}")
        return account_str
