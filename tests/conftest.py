import pytest
from datetime import datetime

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-03-11T02:26:18.671407",
            "operationAmount": {"amount": "1000", "currency": {"name": "USD"}},
            "description": "Перевод",
            "from": "Card 7000792289606361",
            "to": "Account 64686473678894779589"
        },
        {
            "id": 2,
            "state": "PENDING",
            "date": "2024-03-10T15:23:01.802311",
            "operationAmount": {"amount": "2000", "currency": {"name": "RUB"}},
            "description": "Оплата",
            "from": "Card 1234567812345670",
            "to": "Account 98765432109876543210"
        }
    ]