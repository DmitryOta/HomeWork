import json
import os

WEY_TO_FILE = os.path.join(os.path.dirname(__file__), "../data/operations.json")


def unpacking_json(WEY_TO_FILE: str) -> list[dict]:
    """Функция, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    operation_list: list = []
    with open(WEY_TO_FILE, encoding="utf-8") as json_file:
        try:
            data = json.load(json_file)
            if type(data) is not list:
                return operation_list
            else:
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return operation_list
