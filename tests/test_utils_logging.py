"""
Тесты для проверки логирования в модуле utils.
"""
import json
import logging
from pathlib import Path
from unittest.mock import patch, Mock

import pytest

from src.utils import get_transactions_from_json


def test_logging_file_not_found(tmp_path):
    """Тест: логирование ошибки при отсутствии файла"""
    with patch("src.utils.logger") as mock_logger:
        result = get_transactions_from_json("nonexistent.json")
        assert result == []
        mock_logger.error.assert_called_once()
        mock_logger.debug.assert_called()


def test_logging_successful_load(tmp_path):
    """Тест: логирование успешной загрузки"""
    with patch("src.utils.logger") as mock_logger:
        test_file = tmp_path / "test.json"
        test_data = [{"id": 1, "amount": 100}]
        test_file.write_text(json.dumps(test_data))

        result = get_transactions_from_json(str(test_file))
        assert result == test_data
        mock_logger.info.assert_called_once()
        mock_logger.debug.assert_called()


def test_logging_invalid_json(tmp_path):
    """Тест: логирование ошибки при невалидном JSON"""
    with patch("src.utils.logger") as mock_logger:
        test_file = tmp_path / "invalid.json"
        test_file.write_text("not json")

        result = get_transactions_from_json(str(test_file))
        assert result == []
        mock_logger.error.assert_called_once()
