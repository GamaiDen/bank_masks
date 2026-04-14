"""
Тесты для модуля utils.
"""
import json
import pytest
from pathlib import Path
from unittest.mock import patch, Mock
from src.utils import get_transactions_from_json


def test_get_transactions_from_json_file_not_found():
    """Тест: файл не найден - возвращает пустой список"""
    result = get_transactions_from_json("nonexistent_file.json")
    assert result == []


def test_get_transactions_from_json_empty_file(tmp_path):
    """Тест: пустой файл - возвращает пустой список"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("", encoding="utf-8")
    result = get_transactions_from_json(str(empty_file))
    assert result == []


def test_get_transactions_from_json_not_list(tmp_path):
    """Тест: файл содержит не список - возвращает пустой список"""
    not_list_file = tmp_path / "not_list.json"
    not_list_file.write_text('{"key": "value"}', encoding="utf-8")
    result = get_transactions_from_json(str(not_list_file))
    assert result == []


def test_get_transactions_from_json_valid_list(tmp_path):
    """Тест: корректный JSON со списком"""
    valid_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    valid_file = tmp_path / "valid.json"
    valid_file.write_text(json.dumps(valid_data), encoding="utf-8")
    result = get_transactions_from_json(str(valid_file))
    assert result == valid_data


def test_get_transactions_from_json_invalid_json(tmp_path):
    """Тест: некорректный JSON - возвращает пустой список"""
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("this is not json", encoding="utf-8")
    result = get_transactions_from_json(str(invalid_file))
    assert result == []
