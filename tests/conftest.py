import pytest


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми данными транзакций"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T10:30:00"},
        {"id": 2, "state": "PENDING", "date": "2024-03-14T10:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-13T10:30:00"},
        {"id": 4, "state": "CANCELED", "date": "2024-03-12T10:30:00"},
        {"id": 5, "state": "EXECUTED", "date": "2024-03-11T10:30:00"},
    ]


@pytest.fixture
def transactions_same_date():
    """Фикстура с транзакциями, имеющими одинаковую дату"""
    return [
        {"id": 1, "date": "2024-03-15T10:30:00"},
        {"id": 2, "date": "2024-03-15T09:30:00"},
        {"id": 3, "date": "2024-03-15T11:30:00"},
    ]


@pytest.fixture
def empty_transactions():
    """Фикстура с пустым списком транзакций"""
    return []


@pytest.fixture
def sample_card_numbers():
    """Фикстура с примерами номеров карт"""
    return {
        "visa": "1234567890123456",
        "mastercard": "9876543210987654",
        "short": "1234",
        "empty": "",
    }


@pytest.fixture
def sample_account_numbers():
    """Фикстура с примерами номеров счетов"""
    return {
        "valid": "12345678901234567890",
        "short": "123",
        "empty": "",
    }
