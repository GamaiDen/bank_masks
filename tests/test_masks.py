import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"

@pytest.mark.parametrize("card_num,expected", [
    (7000792289606361, "7000 79** **** 6361"),  # ← ПРАВИЛЬНЫЙ ФОРМАТ!
    (1234567812345670, "1234 56** **** 5670"),  # ← ПРАВИЛЬНЫЙ ФОРМАТ!
])
def test_get_mask_card_number_parametrized(card_num, expected):
    assert get_mask_card_number(card_num) == expected
