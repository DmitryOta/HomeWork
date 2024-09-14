import json
import logging
import os

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


WEY_TO_FILE = os.path.join(os.path.dirname(__file__), "../data/operations.json")


def unpacking_json(file: str) -> list[dict]:
    """Функция, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logging.info("Начало работы функции")
    operation_list: list = []
    with open(file, encoding="utf-8") as json_file:
        try:
            data = json.load(json_file)
            logging.info("Выполняем проверку JSON-файла на соответсвие типу list")
            if type(data) is not list:
                return operation_list
            else:
                return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Произошла ошибка: {e}")
            return operation_list
