from .masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета из строки формата 'Visa Platinum 7000792289606361'
    
    Args:
        data (str): Строка с типом и номером карты/счета
        
    Returns:
        str: Строка с замаскированным номером
    """
    parts = data.split()
    if len(parts) < 2:
        return data
    
    card_type = " ".join(parts[:-1])
    number_str = parts[-1]
    
    if card_type.lower() == "счет":
        try:
            account_number = int(number_str)
            masked_number = get_mask_account(account_number)
            return f"{card_type} {masked_number}"
        except ValueError:
            return data
    else:
        try:
            card_number = int(number_str)
            masked_number = get_mask_card_number(card_number)
            return f"{card_type} {masked_number}"
        except ValueError:
            return data


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407' в '11.03.2024'
    
    Args:
        date_str (str): Дата в формате ISO
        
    Returns:
        str: Дата в формате ДД.ММ.ГГГГ
    """
    date_part = date_str.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"
