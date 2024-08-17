import pytest


from src.generators import filter_by_currency, transaction_description, card_number_generator


def test_filter_by_currency(input_transactions):
    usd_transactions = filter_by_currency(input_transactions, "USD")
    assert next(usd_transactions) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(usd_transactions) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }


def test_transaction_description(input_transactions):
    descriptions = transaction_description(input_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


def test_card_number_generator():
    generator = card_number_generator(1,5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"


def test_card_number_generator_max():
    generator = card_number_generator(9999999999999998,)
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"

@pytest.mark.parametrize(
    "start, stop, result",
    [
        (5555555555555555, 5555555555555556, "5555 5555 5555 5555"),
        (6666666666666666, 6666666666666667, "6666 6666 6666 6666"),
        (7777777777777777, 7777777777777778, "7777 7777 7777 7777"),
    ],
)
def test_card_number_generator_split(start, stop, result):
    generator = card_number_generator(start, stop)
    assert next(generator) == result