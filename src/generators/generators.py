"""
Модуль для работы с генераторами транзакций.
"""


def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по валюте и возвращает итератор.

    Args:
        transactions: список словарей с транзакциями
        currency_code: код валюты для фильтрации (например, "USD")

    Yields:
        Словари транзакций в указанной валюте
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор описаний транзакций.

    Args:
        transactions: список словарй с транзакциями

    Yields:
        Описания транзакций по очереди
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """
    Генератор номеров банковских карт.

    Args:
        start: начальный номер карты (int)
        stop: конечный номер карты (int)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for number in range(start, stop + 1):
        # Форматируем номер с ведущими нулями
        card_str = str(number).zfill(16)
        # Разбиваем на группы по 4 цифры
        formatted = " ".join([card_str[i:i + 4] for i in range(0, 16, 4)])
        yield formatted
# Generator functions for transaction processing
