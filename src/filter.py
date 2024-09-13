import re


def filter_transactions(transactions: list[dict], search_string: str):
    pattern = re.compile(search_string)
    filtered_transactions = []
    for transaction in transactions:
        if "description" in transaction and pattern.search(transaction["description"]):
            filtered_transactions.append(transaction)
    return filtered_transactions
