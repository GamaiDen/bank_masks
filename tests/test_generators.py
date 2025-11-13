import pytest

from src.generators.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


class TestFilterByCurrency:
    """Тесты для функции filter_by_currency."""

    def test_filter_usd_transactions(self, sample_transactions):
        """Тест фильтрации USD транзакций."""
        usd_transactions = filter_by_currency(sample_transactions, "USD")
        result = list(usd_transactions)
        assert len(result) == 2
        assert all(
            t["operationAmount"]["currency"]["code"] == "USD"
            for t in result
        )

    def test_filter_rub_transactions(self, sample_transactions):
        """Тест фильтрации RUB транзакций."""
        rub_transactions = filter_by_currency(sample_transactions, "RUB")
        result = list(rub_transactions)
        assert len(result) == 1
        assert result[0]["operationAmount"]["currency"]["code"] == "RUB"

    def test_filter_empty_result(self, sample_transactions):
        """Тест фильтрации с пустым результатом."""
        eur_transactions = filter_by_currency(sample_transactions, "EUR")
        result = list(eur_transactions)
        assert len(result) == 0

    def test_iterator_behavior(self, sample_transactions):
        """Тест поведения итератора."""
        usd_transactions = filter_by_currency(sample_transactions, "USD")
        first = next(usd_transactions)
        assert first["operationAmount"]["currency"]["code"] == "USD"
        second = next(usd_transactions)
        assert second["operationAmount"]["currency"]["code"] == "USD"


class TestTransactionDescriptions:
    """Тесты для генератора transaction_descriptions."""

    def test_descriptions_generator(self, sample_transactions):
        """Тест генератора описаний."""
        descriptions = transaction_descriptions(sample_transactions)
        expected = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет"
        ]
        for expected_desc in expected:
            assert next(descriptions) == expected_desc

    def test_empty_transactions(self):
        """Тест с пустым списком транзакций."""
        descriptions = transaction_descriptions([])
        assert list(descriptions) == []


class TestCardNumberGenerator:
    """Тесты для генератора номеров карт."""

    @pytest.mark.parametrize(
        "start,stop,expected_count,expected_first,expected_last",
        [
            (1, 5, 5, "0000 0000 0000 0001", "0000 0000 0000 0005"),
            (9999999999999995, 9999999999999999, 5,
             "9999 9999 9999 9995", "9999 9999 9999 9999"),
            (1, 1, 1, "0000 0000 0000 0001", "0000 0000 0000 0001"),
        ]
    )
    def test_card_number_generator(
        self, start, stop, expected_count, expected_first, expected_last
    ):
        """Параметризованный тест генератора номеров карт."""
        generator = card_number_generator(start, stop)
        numbers = list(generator)
        assert len(numbers) == expected_count
        assert numbers[0] == expected_first
        assert numbers[-1] == expected_last

    def test_card_number_format(self):
        """Тест формата номеров карт."""
        generator = card_number_generator(1, 1)
        number = next(generator)
        assert len(number) == 19
        parts = number.split(" ")
        assert len(parts) == 4
        assert all(len(part) == 4 for part in parts)
        assert all(part.isdigit() for part in parts)
