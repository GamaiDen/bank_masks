from src.widget import mask_account_card, get_date


def main() -> None:
    """Демонстрация работы новых функций"""

    # Тестовые данные из задания
    test_data = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305"
    ]

    print("=== МАСКИРОВКА КАРТ И СЧЕТОВ ===")
    for data in test_data:
        masked = mask_account_card(data)
        print(f"{data} -> {masked}")

    print("\n=== ПРЕОБРАЗОВАНИЕ ДАТ ===")
    test_dates = [
        "2024-03-11T02:26:18.671407",
        "2023-12-31T23:59:59.999999"
    ]

    for date_str in test_dates:
        formatted_date = get_date(date_str)
        print(f"{date_str} -> {formatted_date}")


if __name__ == "__main__":
    main()
