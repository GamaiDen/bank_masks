from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция принимает строку и возвращает маску счета или карты"""
    if "Счет" in data:
        account_number = data.split()[-1]
        masked_account = get_mask_account(int(account_number))
        return f"Счет {masked_account}"
    else:
        card_number = data.split()[-1]
        masked_card = get_mask_card_number(int(card_number))
        card_name = " ".join(data.split()[:-1])
        return f"{card_name} {masked_card}"


def get_date(date_string: str) -> str:
    """Функция преобразует дату из формата ISO в формат DD.MM.YYYY"""
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")
