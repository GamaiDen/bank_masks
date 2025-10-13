def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты по формату XXXX XX** **** XXXX

    Args:
        card_number (int): Номер карты в виде числа

    Returns:
        str: Замаскированный номер карты
    """
    card_str = str(card_number)

    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета по формату **XXXX

    Args:
        account_number (int): Номер счета в виде числа

    Returns:
        str: Замаскированный номер счета
    """
    account_str = str(account_number)

    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return f"**{account_str[-4:]}"
