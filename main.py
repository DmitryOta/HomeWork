from src.csv_excel import (
    WEY_TO_FILE_CSV,
    WEY_TO_FILE_EXCEL,
    reading_financial_transactions_csv,
    reading_financial_transactions_excel,
)
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.sorting import sorting_transactions
from src.utils import WEY_TO_FILE, unpacking_json


def main():
    """Функция которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой."""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    while True:
        user_num_input = input("Введите номер операции")
        if user_num_input == "1":
            print("Для обработки выбран JSON-файл.")
            file = unpacking_json(WEY_TO_FILE)
            break
        elif user_num_input == "2":
            print("Для обработки выбран CSV-файл.")
            file = reading_financial_transactions_csv(WEY_TO_FILE_CSV)
            break
        elif user_num_input == "3":
            print("Для обработки выбран XLSX-файл.")
            file = reading_financial_transactions_excel(WEY_TO_FILE_EXCEL)
            break
        else:
            print("Попробуйте еще раз")

    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    while True:
        user_status_input = input().upper()
        if user_status_input in ["EXECUTED", "CANCELED", "PENDING"]:
            filters = filter_by_state(file, user_status_input)
            break
        else:
            print(f'Статус операции "{user_status_input}" недоступен.')

    print("Отсортировать операции по дате? Да/Нет")
    while True:
        users_input = input().lower()
        if users_input == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            while True:
                users_input_min_max = input().lower()
                if users_input_min_max == "возрастанию":
                    sorting = False
                    sort_data = sort_by_date(filters, sorting)
                    break
                elif users_input_min_max == "убыванию":
                    sort_data = sort_by_date(filters)
                    break
                else:
                    print("Ответ может быть возрастанию или убыванию.")
        elif users_input == "нет":
            sort_data = filters
            break
        else:
            print("Ответ может быть Да или Нет.")
        break
    print("Выводить только рублевые тразакции? Да/Нет")

    while True:
        user_input = input().lower()
        if user_input == "да":
            currency = "RUB"
            transaction = filter_by_currency(sort_data, currency)
            break
        elif user_input == "нет":
            transaction = sort_data
            break
        else:
            print("Ответ может быть Да или Нет.")

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        user_input = input().lower()
        if user_input == "да":
            word_input = input("Введите слово")
            sorted = sorting_transactions(transaction, word_input)
            break
        elif user_input == "нет":
            sorted = transaction
            break
        else:
            print("Ответ может быть Да или Нет.")
    if len(list(sorted)) < 1:
        return """Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"""
    else:
        return list(sorted)


print(main())
