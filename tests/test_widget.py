import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """Тест маскировки карт и счетов"""
    # Тест для карт
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

    # Тест для счетов
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


def test_get_date() -> None:
    """Тест преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-31T23:59:59.999999") == "31.12.2023"
    assert get_date("2024-01-01T00:00:00.000000") == "01.01.2024"


def test_mask_account_card_validation() -> None:
    """Тест валидации входных данных"""
    with pytest.raises(ValueError):
        mask_account_card("")  # Пустая строка

    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum ABC123")  # Нечисловой номер
