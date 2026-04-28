from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_or_card: str) -> str:
    """
    Принимает строку с типом и номером карты/счета, возвращает замаскированную версию
    Примеры:
    - "Visa Platinum 1234567890123456" -> "Visa Platinum 1234 56** **** 3456"
    - "Счет 12345678901234567890" -> "Счет **7890"
    """
    # Разделяем тип и номер
    parts = account_or_card.rsplit(" ", 1)
    if len(parts) != 2:
        raise ValueError("Не удалось определить тип и номер")

    card_type, number = parts

    # Проверяем, что номер состоит только из цифр (или содержит цифры)
    # Для счета и карты номер должен содержать только цифры
    if not number or not number.isdigit():
        raise ValueError("Не удалось определить тип и номер")

    # Проверяем минимальную длину номера
    if len(number) < 4:
        raise ValueError("Не удалось определить тип и номер")

    try:
        if card_type.lower() == "счет":
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)
    except ValueError:
        raise ValueError("Не удалось определить тип и номер")

    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ
    Пример: "2024-03-15T10:30:00" -> "15.03.2024"
    """
    if not date_string:
        raise ValueError("Пустая строка даты")

    try:
        # Извлекаем только часть с датой
        date_part = date_string.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except (IndexError, ValueError):
        raise ValueError("Неверный формат даты")