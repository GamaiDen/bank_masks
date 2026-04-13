"""
Тесты для проверки логирования в модуле masks.
"""
import logging
from unittest.mock import patch

from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_logging_success():
    """Тест: логирование успешной маскировки карты"""
    with patch("src.masks.logger") as mock_logger:
        result = get_mask_card_number("7000792289606361")
        assert result == "7000 79** **** 6361"
        mock_logger.info.assert_called_once()
        mock_logger.debug.assert_called()


def test_mask_card_logging_error():
    """Тест: логирование ошибки при неверном формате карты"""
    with patch("src.masks.logger") as mock_logger:
        result = get_mask_card_number("123")
        mock_logger.error.assert_called_once()


def test_mask_account_logging_success():
    """Тест: логирование успешной маскировки счета"""
    with patch("src.masks.logger") as mock_logger:
        result = get_mask_account("73654108430135874305")
        assert result == "**4305"
        mock_logger.info.assert_called_once()
        mock_logger.debug.assert_called()


def test_mask_account_logging_error():
    """Тест: логирование ошибки при пустом счете"""
    with patch("src.masks.logger") as mock_logger:
        result = get_mask_account("")
        mock_logger.error.assert_called_once()
