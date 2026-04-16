"""
Вспомогательные функции для работы с данными.
"""

import pandas as pd
from pathlib import Path


def load_transactions(file_path: str) -> pd.DataFrame:
    """
    Загружает транзакции из Excel-файла.

    Аргументы:
        file_path (str): Путь к Excel-файлу.

    Возвращает:
        pd.DataFrame: Датафрейм с транзакциями.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")

    df = pd.read_excel(path)
    # Переименовываем колонки для удобства (если нужно)
    df.columns = df.columns.str.strip()
    return df

import json
import logging
import os
from datetime import datetime, time
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def get_greeting() -> str:
    """
    Возвращает приветствие в зависимости от текущего времени.

    Returns:
        str: Приветствие (Доброе утро/Добрый день/Добрый вечер/Доброй ночи).
    """
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_currency_rates(currencies: List[str]) -> List[Dict[str, Any]]:
    """
    Получает курсы валют через API.

    Args:
        currencies: Список кодов валют.

    Returns:
        Список словарей с курсами валют.
    """
    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        logger.warning("EXCHANGE_API_KEY не задан, возвращаем тестовые данные")
        return [{"currency": curr, "rate": 1.0} for curr in currencies]

    rates = []
    for currency in currencies:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
            response = requests.get(url, headers={"apikey": api_key}, timeout=10)
            response.raise_for_status()
            data = response.json()
            rate = data.get("rates", {}).get("RUB", 0.0)
            rates.append({"currency": currency, "rate": rate})
        except Exception as e:
            logger.error(f"Ошибка получения курса {currency}: {e}")
            rates.append({"currency": currency, "rate": 0.0})

    return rates


def get_stock_prices(stocks: List[str]) -> List[Dict[str, Any]]:
    """
    Получает цены акций через API.

    Args:
        stocks: Список тикеров акций.

    Returns:
        Список словарей с ценами акций.
    """
    api_key = os.getenv("STOCK_API_KEY")
    if not api_key:
        logger.warning("STOCK_API_KEY не задан, возвращаем тестовые данные")
        return [{"stock": stock, "price": 100.0} for stock in stocks]

    prices = []
    for stock in stocks:
        try:
            # Используем Alpha Vantage API (бесплатный)
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            price = float(data.get("Global Quote", {}).get("05. price", 0))
            prices.append({"stock": stock, "price": price})
        except Exception as e:
            logger.error(f"Ошибка получения цены {stock}: {e}")
            prices.append({"stock": stock, "price": 0.0})

    return prices


def load_user_settings(file_path: str = "user_settings.json") -> Dict[str, List[str]]:
    """
    Загружает настройки пользователя из JSON-файла.

    Args:
        file_path: Путь к файлу настроек.

    Returns:
        Словарь с настройками.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Ошибка загрузки настроек: {e}")
        return {"user_currencies": [], "user_stocks": []}
