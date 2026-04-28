import pytest
from src.widget import mask_account_card, get_date

class TestMaskAccountCard:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
            ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
            ("Счет 12345678901234567890", "Счет **7890"),
            ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
            ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ],
    )
    def test_mask_account_card_valid(self, input_data, expected):
        assert mask_account_card(input_data) == expected

    def test_mask_account_card_invalid(self):
        with pytest.raises(ValueError):
            mask_account_card("Invalid data")

    def test_mask_account_card_no_number(self):
        with pytest.raises(ValueError):
            mask_account_card("Visa Platinum")

    def test_mask_account_card_empty(self):
        with pytest.raises(ValueError):
            mask_account_card("")

class TestGetDate:
    @pytest.mark.parametrize(
        "date_string, expected",
        [
            ("2024-03-15T10:30:00", "15.03.2024"),
            ("2023-12-25T08:15:00", "25.12.2023"),
            ("2024-01-01T00:00:00", "01.01.2024"),
            ("2024-12-31T23:59:59", "31.12.2024"),
        ],
    )
    def test_get_date_valid(self, date_string, expected):
        assert get_date(date_string) == expected

    def test_get_date_empty(self):
        with pytest.raises(ValueError, match="Пустая строка даты"):
            get_date("")

    def test_get_date_invalid_format(self):
        with pytest.raises(ValueError, match="Неверный формат даты"):
            get_date("15.03.2024")

    def test_get_date_no_time(self):
        assert get_date("2024-03-15") == "15.03.2024"