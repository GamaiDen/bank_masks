"""
Модуль для конвертации валют через внешнее API.
"""
import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Аргументы:
        transaction (Dict[str, Any]): Словарь с данными транзакции.

    Возвращает:
        float: Сумма в рублях. Если транзакция в USD или EUR - конвертирует через API.
    """
    # Получаем данные о сумме операции
    operation_amount = transaction.get("operationAmount")
    if not operation_amount:
        return 0.0

    # Получаем сумму
    amount = operation_amount.get("amount")
    if amount is None:
        return 0.0

    # Преобразуем сумму в число
    try:
        amount_float = float(amount)
    except (ValueError, TypeError):
        return 0.0

    # Получаем код валюты
    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code", "")

    # Если рубли - возвращаем сумму
    if currency_code.upper() == "RUB":
        return amount_float

    # Если не USD и не EUR - возвращаем 0
    if currency_code.upper() not in ("USD", "EUR"):
        return 0.0

    # Конвертируем через API
    if not API_KEY:
        return 0.0

    try:
        response = requests.get(
            BASE_URL,
            headers={"apikey": API_KEY},
            params={
                "from": currency_code.upper(),
                "to": "RUB",
                "amount": amount_float
            },
            timeout=10
        )
        response.raise_for_status()
        result = response.json().get("result")
        return float(result) if result is not None else 0.0
    except (requests.RequestException, ValueError, KeyError, Exception):
        # Ловим ошибки API
        return 0.0
