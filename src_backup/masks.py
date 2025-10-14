def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX
    
    Args:
        card_number (int): Номер карты
        
    Returns:
        str: Замаскированный номер карты
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета в формате **XXXX
    
    Args:
        account_number (int): Номер счета
        
    Returns:
        str: Замаскированный номер счета
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
