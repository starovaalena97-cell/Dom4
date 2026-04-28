def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, показывая первые 6 и последние 4 цифры
    Пример: 1234567890123456 -> "1234 56** **** 3456"
    """
    if not card_number:
        return ""
    if len(card_number) < 6:
        raise ValueError("Номер карты слишком короткий")

    # Формат: XXXX XX** **** XXXX
    first_part = card_number[:4]  # первые 4 цифры
    second_part = card_number[4:6]  # следующие 2 цифры
    last_part = card_number[-4:]  # последние 4 цифры

    return f"{first_part} {second_part}** **** {last_part}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры
    Пример: 12345678901234567890 -> "**7890"
    """
    if not account_number:
        return ""
    if len(account_number) < 4:
        raise ValueError("Номер счета слишком короткий")

    return f"**{account_number[-4:]}"
