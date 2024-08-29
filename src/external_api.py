import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_amount_transaction(transaction: dict) -> float | bool:
    """Функция возвращает сумму транзакции в рублях если транзакция была в другой валюте функция переведет в рубли"""
    if not transaction or not transaction.get("operationAmount"):
        return False
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if code == "RUB":
        return float(amount)
    else:
        api_token = os.getenv("MY_KEY_API")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": api_token}
        response = requests.get(url, headers=headers)

        status_code = response.status_code
        print(status_code)
        result = response.json()
        if status_code == 200:
            return float(round(result["result"], 2))
        return False
