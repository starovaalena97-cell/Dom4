from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список транзакций по заданному статусу
    """
    if not transactions:
        return []

    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате
    reverse=True - по убыванию (новые сверху)
    reverse=False - по возрастанию (старые сверху)
    """
    if not transactions:
        return []

    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)