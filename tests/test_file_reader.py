"""
Тесты для модуля file_reader.
"""
from unittest.mock import Mock, patch

from src.file_reader import (read_transactions_from_csv,
                             read_transactions_from_excel)


def test_read_transactions_from_csv_success():
    """Тест: успешное чтение CSV файла"""
    with patch("pandas.read_csv") as mock_read_csv:
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
        mock_read_csv.return_value = mock_df

        result = read_transactions_from_csv("fake.csv")
        assert result == [{"id": 1, "amount": 100}]
        mock_read_csv.assert_called_once_with("fake.csv")


def test_read_transactions_from_csv_file_not_found():
    """Тест: файл не найден"""
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = read_transactions_from_csv("nonexistent.csv")
        assert result == []


def test_read_transactions_from_csv_empty():
    """Тест: пустой CSV файл"""
    with patch("pandas.read_csv") as mock_read_csv:
        mock_df = Mock()
        mock_df.empty = True
        mock_read_csv.return_value = mock_df

        result = read_transactions_from_csv("empty.csv")
        assert result == []


def test_read_transactions_from_excel_success():
    """Тест: успешное чтение Excel файла"""
    with patch("pandas.read_excel") as mock_read_excel:
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_dict.return_value = [{"id": 1, "amount": 200}]
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel("fake.xlsx")
        assert result == [{"id": 1, "amount": 200}]
        mock_read_excel.assert_called_once_with("fake.xlsx", engine='openpyxl')


def test_read_transactions_from_excel_file_not_found():
    """Тест: Excel файл не найден"""
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_transactions_from_excel("nonexistent.xlsx")
        assert result == []


def test_read_transactions_from_excel_empty():
    """Тест: пустой Excel файл"""
    with patch("pandas.read_excel") as mock_read_excel:
        mock_df = Mock()
        mock_df.empty = True
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel("empty.xlsx")
        assert result == []
