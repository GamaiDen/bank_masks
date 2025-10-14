from .masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета из строки формата 'Visa Platinum 7000792289606361'
    
    Args:
        data (str): Строка с типом и номером карты/счета
        
    Returns:
        str: Строка с замаскированным номером
    """
    # Разделяем на тип и номер
    parts = data.split()
    if len(parts) < 2:
        return data
    
    # Определяем тип (карта или счет)
    card_type = " ".join(parts[:-1])  # Все слова кроме последнего
    number_str = parts[-1]  # Последнее слово - номер
    
    # Проверяем, это счет или карта
    if card_type.lower() == "счет":
        # Для счета используем get_mask_account
        try:
            account_number = int(number_str)
            masked_number = get_mask_account(account_number)
            return f"{card_type} {masked_number}"
        except ValueError:
            return data
    else:
        # Для карты используем get_mask_card_number
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
    # Берем только часть до T (дату)
    date_part = date_str.split('T')[0]
    
    # Разделяем на год, месяц, день
    year, month, day = date_part.split('-')
    
    # Возвращаем в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"
