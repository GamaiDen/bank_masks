"""
Тесты для модуля external_api.
"""
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub


def test_convert_to_rub_rub():
    """Тест: транзакция в рублях"""
    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"name": "руб.", "code": "RUB"}
        }
    }
    result = convert_to_rub(transaction)
    assert result == 1000.0


def test_convert_to_rub_missing_operation_amount():
    """Тест: отсутствует operationAmount"""
    assert convert_to_rub({}) == 0.0
    assert convert_to_rub({"operationAmount": {}}) == 0.0


def test_convert_to_rub_invalid_amount():
    """Тест: некорректная сумма"""
    transaction = {
        "operationAmount": {
            "amount": "not a number",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_to_rub(transaction)
    assert result == 0.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_success(mock_get):
    """Тест: успешная конвертация USD -> RUB"""
    with patch("src.external_api.API_KEY", "test_api_key"):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "result": 9500.0}
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "доллар", "code": "USD"}
            }
        }
        result = convert_to_rub(transaction)
        assert result == 9500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get):
    """Тест: ошибка API - возвращаем 0.0"""
    with patch("src.external_api.API_KEY", "test_api_key"):
        mock_get.side_effect = Exception("API unavailable")
        transaction = {
            "operationAmount": {
                "amount": "50.00",
                "currency": {"code": "EUR"}
            }
        }
        result = convert_to_rub(transaction)
        assert result == 0.0


def test_convert_to_rub_unsupported_currency():
    """Тест: неподдерживаемая валюта"""
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "GBP"}
        }
    }
    result = convert_to_rub(transaction)
    assert result == 0.0


def test_convert_to_rub_no_api_key():
    """Тест: нет API ключа"""
    with patch("src.external_api.API_KEY", None):
        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"}
            }
        }
        result = convert_to_rub(transaction)
        assert result == 0.0
