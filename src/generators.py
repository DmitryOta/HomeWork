def filter_by_currency(transactions, currency="USD"):
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции USD"""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_description(transactions):
    """Функция-генератор, которая принимает список словарей
    с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start=1, stop=10000000000000000):
    """Функция-генератор , которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    , где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for i in range(start, stop):
        num = 10000000000000000 + i
        str_num = str(num)
        yield str_num[1:5] + " " + str_num[5:9] + " " + str_num[9:13] + " " + str_num[13:17]
