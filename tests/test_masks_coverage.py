"""
Дополнительные тесты для повышения покрытия masks.py.
"""
from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_number_with_spaces():
    """Тест: номер карты с пробелами"""
    result = get_mask_card_number("7000 7922 8960 6361")
    assert result == "7000 79** **** 6361"


def test_mask_card_number_too_short():
    """Тест: слишком короткий номер карты"""
    result = get_mask_card_number("123456")
    assert result == "123456"


def test_mask_card_number_with_letters():
    """Тест: номер карты с буквами - возвращаем исходную строку"""
    result = get_mask_card_number("7000abcd89606361")
    assert result == "7000abcd89606361"


def test_mask_account_too_short():
    """Тест: слишком короткий номер счета"""
    result = get_mask_account("123")
    assert result == "123"


def test_mask_account_with_spaces():
    """Тест: номер счета с пробелами"""
    result = get_mask_account("7365 4108 4301 3587 4305")
    assert result == "**4305"
