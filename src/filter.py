import re


def filter_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция, принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка."""
    pattern = re.compile(search_string.lower())
    filtered_transactions = []
    for transaction in transactions:
        if "description" in transaction and pattern.search(transaction["description"].lower()):
            filtered_transactions.append(transaction)
    return filtered_transactions
