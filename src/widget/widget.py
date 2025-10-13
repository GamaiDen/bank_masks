from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа

    Args:
        data (str): Строка с типом и номером карты/счета

    Returns:
        str: Строка с замаскированным номером
    """
    parts = data.split()

    if not parts:
        raise ValueError("Пустая строка")

    # Определяем тип (последнее слово перед номером)
    account_type = " ".join(parts[:-1])
    number = parts[-1]

    # Проверяем является ли номер числом
    if not number.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    # Определяем тип операции (карта или счет)
    if "счет" in data.lower() or "account" in data.lower():
        masked_number = get_mask_account(int(number))
    else:
        masked_number = get_mask_card_number(int(number))

    return f"{account_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ

    Args:
        date_str (str): Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "11.03.2024"
    """
    # Разделяем дату и время
    date_part = date_str.split("T")[0]

    # Разбиваем на год, месяц, день
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
