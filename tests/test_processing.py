import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T10:30:00"},
        {"id": 2, "state": "PENDING", "date": "2024-03-14T10:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-13T10:30:00"},
        {"id": 4, "state": "CANCELED", "date": "2024-03-12T10:30:00"},
        {"id": 5, "state": "EXECUTED", "date": "2024-03-11T10:30:00"},
    ]

@pytest.fixture
def transactions_same_date():
    return [
        {"id": 1, "date": "2024-03-15T10:30:00"},
        {"id": 2, "date": "2024-03-15T09:30:00"},
        {"id": 3, "date": "2024-03-15T11:30:00"},
    ]

@pytest.fixture
def empty_transactions():
    return []

class TestFilterByState:
    @pytest.mark.parametrize(
        "state, expected_ids",
        [
            ("EXECUTED", [1, 3, 5]),
            ("PENDING", [2]),
            ("CANCELED", [4]),
            ("NON_EXISTENT", []),
        ],
    )
    def test_filter_by_state(self, sample_transactions, state, expected_ids):
        result = filter_by_state(sample_transactions, state)
        result_ids = [item["id"] for item in result]
        assert result_ids == expected_ids

    def test_filter_by_state_default(self, sample_transactions):
        result = filter_by_state(sample_transactions)
        result_ids = [item["id"] for item in result]
        assert result_ids == [1, 3, 5]

    def test_filter_by_state_empty(self, empty_transactions):
        assert filter_by_state(empty_transactions, "EXECUTED") == []

    def test_filter_by_state_missing_key(self):
        transactions = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "amount": 100},
        ]
        result = filter_by_state(transactions, "EXECUTED")
        result_ids = [item["id"] for item in result]
        assert result_ids == [1]

class TestSortByDate:
    def test_sort_descending(self, sample_transactions):
        result = sort_by_date(sample_transactions)
        dates = [item["date"] for item in result]
        assert dates == [
            "2024-03-15T10:30:00",
            "2024-03-14T10:30:00",
            "2024-03-13T10:30:00",
            "2024-03-12T10:30:00",
            "2024-03-11T10:30:00",
        ]

    def test_sort_ascending(self, sample_transactions):
        result = sort_by_date(sample_transactions, reverse=False)
        dates = [item["date"] for item in result]
        assert dates == [
            "2024-03-11T10:30:00",
            "2024-03-12T10:30:00",
            "2024-03-13T10:30:00",
            "2024-03-14T10:30:00",
            "2024-03-15T10:30:00",
        ]

    def test_sort_same_dates(self, transactions_same_date):
        result = sort_by_date(transactions_same_date, reverse=False)
        ids = [item["id"] for item in result]
        assert ids == [2, 1, 3]

    def test_sort_empty(self, empty_transactions):
        assert sort_by_date(empty_transactions) == []

    def test_sort_single_element(self):
        transactions = [{"id": 1, "date": "2024-03-15T10:30:00"}]
        result = sort_by_date(transactions)
        assert result == transactions