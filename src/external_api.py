"""
Модуль для конвертации валют через внешнее API.
"""
import os
<<<<<<< HEAD
from typing import Dict, Any
=======
from typing import Any, Dict
>>>>>>> a0698861399be6f9e192f762298ffe8731c117df

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
    operation_amount = transaction.get("operationAmount")
    if not operation_amount:
        return 0.0

    amount = operation_amount.get("amount")
    if amount is None:
        return 0.0

    try:
        amount_float = float(amount)
    except (ValueError, TypeError):
        return 0.0

    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code", "")

    if currency_code.upper() == "RUB":
        return amount_float

    if currency_code.upper() not in ("USD", "EUR"):
        return 0.0

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
    except Exception:
        return 0.0
