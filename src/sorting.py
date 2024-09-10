import re
from collections import Counter


def sorting_transactions(transactoins: list[dict], search_bar: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска, а возвращает
    список словарей, у которых в описании есть данная строка"""
    pattern = re.compile(search_bar.lower())
    result = []
    for transactoin in transactoins:
        if pattern.search(transactoin["description"].lower()):
            result.append(transactoin["description"])
    return result


def count_categories(transactions: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, и возвращает
     словарь, где ключами являются названия категорий, а значениями — количество операций в каждой категории.
    """
    category_counts = []

    for transaction in transactions:
        for category in categories:
            if category in transaction["description"].lower():
                category_counts.append(transaction["description"])
    counted = Counter(category_counts)
    return counted
