"""
Главный запускной модуль курсовой работы.
"""

import json

from src.reports import spending_by_category
from src.services import simple_search
from src.utils import load_transactions
from src.views import main_page


def run_coursework():
    """Демонстрация работы всех функций курсовой."""
    print("=== КУРСОВАЯ РАБОТА ===\n")

    # 1. Главная страница
    print("1. Главная страница (на 31.12.2021):")
    result = main_page("2021-12-31 23:59:59")
    data = json.loads(result)
    print(f"   Приветствие: {data['greeting']}")
    print(f"   Карт: {len(data['cards'])}")
    print(f"   Топ-транзакций: {len(data['top_transactions'])}")
    print(f"   Валют: {len(data['currency_rates'])}")
    print(f"   Акций: {len(data['stock_prices'])}\n")

    # 2. Простой поиск
    print("2. Простой поиск ('ozon'):")
    df = load_transactions("data/operations.xlsx")
    transactions = df.to_dict("records")
    search_result = simple_search(transactions, "ozon")
    search_data = json.loads(search_result)
    print(f"   Найдено транзакций: {len(search_data)}\n")

    # 3. Траты по категории
    print("3. Траты по категории 'Супермаркеты':")
    report = spending_by_category(df, "Супермаркеты", "2021-12-31")
    print(f"   Найдено транзакций: {len(report)}")
    print(f"   Сумма: {report['Сумма операции'].sum():.2f} руб.\n")

    print("=== ГОТОВО ===")


if __name__ == "__main__":
    run_coursework()
