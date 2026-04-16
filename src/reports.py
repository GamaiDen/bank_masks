"""
Модуль для генерации отчетов по транзакциям.
"""

import json
import logging
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, Callable, Optional

import pandas as pd

logger = logging.getLogger(__name__)


def save_to_file(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для сохранения результата функции в файл.

    Args:
        filename: Имя файла. Если None — генерируется автоматически.

    Returns:
        Декорированная функция.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Генерируем имя файла
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{func.__name__}_{timestamp}.json"
            else:
                file_name = filename

            # Сохраняем результат
            with open(file_name, "w", encoding="utf-8") as f:
                if isinstance(result, pd.DataFrame):
                    f.write(result.to_json(orient="records", force_ascii=False, indent=2))
                else:
                    json.dump(result, f, ensure_ascii=False, indent=2)

            logger.info(f"Результат сохранен в {file_name}")
            return result

        return wrapper
    return decorator


@save_to_file()
def spending_by_category(
    transactions: pd.DataFrame,
    category: str,
    date: Optional[str] = None
) -> pd.DataFrame:
    """
    Возвращает траты по заданной категории за последние три месяца.

    Args:
        transactions: Датафрейм с транзакциями.
        category: Название категории.
        date: Дата отсчета в формате YYYY-MM-DD. Если None — текущая дата.

    Returns:
        Датафрейм с тратами по категории за последние 3 месяца.
    """
    logger.info(f"Расчет трат по категории '{category}' на дату {date}")

    # Определяем дату отсчета
    if date is None:
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(date, "%Y-%m-%d")

    start_date = end_date - timedelta(days=90)

    # Копируем и фильтруем
    df = transactions.copy()
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)

    mask = (
        (df["Дата операции"] >= start_date)
        & (df["Дата операции"] <= end_date)
        & (df["Категория"] == category)
        & (df["Сумма операции"] < 0)  # Только расходы
    )

    result_df = df[mask].copy()
    result_df["Сумма операции"] = result_df["Сумма операции"].abs()

    logger.info(f"Найдено {len(result_df)} транзакций на сумму {result_df['Сумма операции'].sum():.2f}")

    return result_df[["Дата операции", "Сумма операции", "Категория", "Описание"]]
