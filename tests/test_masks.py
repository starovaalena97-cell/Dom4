import pytest
from src.masks import get_mask_card_number, get_mask_account

class TestGetMaskCardNumber:
    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("1234567890123456", "1234 56** **** 3456"),
            ("1111222233334444", "1111 22** **** 4444"),
            ("5555666677778888", "5555 66** **** 8888"),
            ("9876543210987654", "9876 54** **** 7654"),
        ],
    )
    def test_mask_card_number_valid(self, card_number, expected):
        assert get_mask_card_number(card_number) == expected

    def test_mask_card_number_empty(self):
        assert get_mask_card_number("") == ""

    def test_mask_card_number_short(self):
        with pytest.raises(ValueError, match="Номер карты слишком короткий"):
            get_mask_card_number("1234")


class TestGetMaskAccount:
    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("12345678901234567890", "**7890"),
            ("98765432109876543210", "**3210"),
            ("0000111122223333", "**3333"),
        ],
    )
    def test_mask_account_valid(self, account_number, expected):
        assert get_mask_account(account_number) == expected

    def test_mask_account_empty(self):
        assert get_mask_account("") == ""

    def test_mask_account_short(self):
        with pytest.raises(ValueError, match="Номер счета слишком короткий"):
            get_mask_account("123")

    def test_mask_account_boundary(self):
        """Тест с номером счета длиной ровно 4 символа"""
        assert get_mask_account("1234") == "**1234"