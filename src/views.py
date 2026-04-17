"""
Модуль для генерации JSON-ответов для веб-страниц.
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import pandas as pd

from src.utils import (
    get_currency_rates,
    get_greeting,
    get_stock_prices,
    load_user_settings,
    load_transactions,
)

logger = logging.getLogger(__name__)


def get_cards_info(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Получает информацию по каждой карте: последние 4 цифры, сумма расходов, кешбэк.

    Args:
        df: Датафрейм с транзакциями.

    Returns:
        Список словарей с информацией по картам.
    """
    cards = []
    # Группируем по номеру карты (последние 4 цифры)
    df_copy = df.copy()
    df_copy["last_digits"] = df_copy["Номер карты"].astype(str).str[-4:]

    for card_number in df_copy["last_digits"].unique():
        if pd.isna(card_number) or card_number == "nan":
            continue

        card_df = df_copy[df_copy["last_digits"] == card_number]
        # Только расходные операции (сумма > 0)
        spent_df = card_df[card_df["Сумма операции"] < 0]
        total_spent = abs(spent_df["Сумма операции"].sum())
        cashback = total_spent / 100

        cards.append({
            "last_digits": card_number,
            "total_spent": round(total_spent, 2),
            "cashback": round(cashback, 2),
        })

    return cards


def get_top_transactions(df: pd.DataFrame, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Получает топ-N транзакций по сумме платежа.

    Args:
        df: Датафрейм с транзакциями.
        limit: Количество транзакций.

    Returns:
        Список словарей с топ-транзакциями.
    """
    # Сортируем по сумме платежа по убыванию
    top_df = df.nlargest(limit, "Сумма платежа")

    result = []
    for _, row in top_df.iterrows():
        result.append({
            "date": row["Дата операции"].strftime("%d.%m.%Y") if pd.notna(row["Дата операции"]) else "",
            "amount": row["Сумма платежа"],
            "category": row["Категория"] if pd.notna(row["Категория"]) else "",
            "description": row["Описание"] if pd.notna(row["Описание"]) else "",
        })

    return result


def main_page(date_str: str) -> str:
    """
    Главная страница — возвращает JSON-ответ с приветствием, информацией по картам,
    топ-транзакциями, курсами валют и ценами акций.

    Args:
        date_str: Дата и время в формате YYYY-MM-DD HH:MM:SS.

    Returns:
        JSON-строка с данными для главной страницы.
    """
    logger.info(f"Генерация главной страницы на {date_str}")

    # Парсим дату
    target_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    start_date = target_date.replace(day=1, hour=0, minute=0, second=0)

    # Загружаем транзакции
    df = load_transactions("data/operations.xlsx")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)

    # Фильтруем с начала месяца до целевой даты
    mask = (df["Дата операции"] >= start_date) & (df["Дата операции"] <= target_date)
    filtered_df = df[mask]

    # Загружаем настройки
    settings = load_user_settings()

    # Формируем ответ
    response: Dict[str, Any] = {
        "greeting": get_greeting(),
        "cards": get_cards_info(filtered_df),
        "top_transactions": get_top_transactions(filtered_df),
        "currency_rates": get_currency_rates(settings.get("user_currencies", [])),
        "stock_prices": get_stock_prices(settings.get("user_stocks", [])),
    }

    return json.dumps(response, ensure_ascii=False, indent=2)
