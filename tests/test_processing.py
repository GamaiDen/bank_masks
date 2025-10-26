import pytest
from src.processing import filter_by_state, sort_by_date


class TestProcessing:
    def test_filter_by_state_executed(self, sample_transactions):
        result = filter_by_state(sample_transactions, "EXECUTED")
        assert len(result) == 1
        assert result[0]["state"] == "EXECUTED"

    def test_filter_by_state_pending(self, sample_transactions):
        result = filter_by_state(sample_transactions, "PENDING")
        assert len(result) == 1
        assert result[0]["state"] == "PENDING"

    def test_sort_by_date_desc(self, sample_transactions):
        result = sort_by_date(sample_transactions)
        # Проверяем что более поздняя дата идет первой
        assert result[0]["date"] > result[1]["date"]