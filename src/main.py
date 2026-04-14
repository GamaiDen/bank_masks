"""
Главный модуль программы для работы с банковскими транзакциями.
"""

from typing import Any, Dict, List

from src.file_reader import (read_transactions_from_csv,
                             read_transactions_from_excel)
from src.processing import filter_by_state, sort_by_date
from src.search import search_by_description
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card


def print_transaction(transaction: Dict[str, Any]) -> None:
    """Выводит одну транзакцию в форматированном виде."""
    date_str = get_date(transaction.get("date", ""))
    description = transaction.get("description", "")

    from_account = transaction.get("from", "")
    to_account = transaction.get("to", "")

    if from_account:
        from_masked = mask_account_card(from_account)
    else:
        from_masked = "Нет данных"

    if to_account:
        to_masked = mask_account_card(to_account)
    else:
        to_masked = "Нет данных"

    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount", "0")
    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code", "")

    print(f"{date_str} {description}")
    if from_masked != "Нет данных" and to_masked != "Нет данных":
        print(f"{from_masked} -> {to_masked}")
    else:
        if to_masked != "Нет данных":
            print(f"{to_masked}")
    print(f"Сумма: {amount} {currency_code}")
    print()


def filter_by_currency_rub(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Оставляет только рублевые транзакции."""
    result = []
    for t in transactions:
        op_amount = t.get("operationAmount", {})
        currency_info = op_amount.get("currency", {})
        if currency_info.get("code") == "RUB":
            result.append(t)
    return result


def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    """Получает от пользователя выбор из списка допустимых значений."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_choices:
            return user_input
        print(f'Неверный ввод. Допустимые значения: {", ".join(valid_choices)}')


def get_status_choice() -> str:
    """Получает от пользователя статус для фильтрации."""
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status_input = input().strip().upper()
        if status_input in valid_statuses:
            return status_input
        print(f'Статус операции "{status_input}" недоступен.')


def main() -> None:
    """Главная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    transactions: List[Dict[str, Any]] = []
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_transactions_from_json("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Программа завершена.")
        return

    if not transactions:
        print("Не найдено ни одной транзакции.")
        return

    status = get_status_choice()
    filtered_transactions = filter_by_state(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_choice = get_user_choice("Отсортировать операции по дате? Да/Нет: ", ["да", "нет"])
    if sort_choice == "да":
        sort_order = get_user_choice(
            "Отсортировать по возрастанию или по убыванию? ",
            ["по возрастанию", "по убыванию"]
        )
        reverse = sort_order == "по убыванию"
        filtered_transactions = sort_by_date(filtered_transactions, reverse)

    rub_choice = get_user_choice("Выводить только рублевые транзакции? Да/Нет: ", ["да", "нет"])
    if rub_choice == "да":
        filtered_transactions = filter_by_currency_rub(filtered_transactions)

    search_choice = get_user_choice(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ",
        ["да", "нет"]
    )
    if search_choice == "да":
        search_word = input("Введите слово для поиска: ").strip()
        if search_word:
            filtered_transactions = search_by_description(filtered_transactions, search_word)

    print("\nРаспечатываю итоговый список транзакций...\n")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
    for transaction in filtered_transactions:
        print_transaction(transaction)


if __name__ == "__main__":
    main()
