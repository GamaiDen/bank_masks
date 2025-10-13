import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тест маскировки номера карты"""
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"


def test_get_mask_account() -> None:
    """Тест маскировки номера счета"""
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(12345678901234567890) == "**7890"


def test_card_number_validation() -> None:
    """Тест валидации номера карты"""
    with pytest.raises(ValueError):
        get_mask_card_number(123)


def test_account_validation() -> None:
    """Тест валидации номера счета"""
    with pytest.raises(ValueError):
        get_mask_account(123)
