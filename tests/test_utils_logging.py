"""
Тесты для проверки логирования в модуле utils.
"""
from unittest.mock import patch

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
        test_file.write_text('[{"id": 1, "amount": 100}]')
        result = get_transactions_from_json(str(test_file))
        assert result == [{"id": 1, "amount": 100}]
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
