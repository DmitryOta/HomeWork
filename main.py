def main():
    print("""Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        user_num_input = int(input("Введите номер операции"))
        if user_num_input == 1:
            print("Для обработки выбран JSON-файл.")
            break
        elif user_num_input == 2:
            print("Для обработки выбран CSV-файл.")
            break
        elif user_num_input == 3:
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Попробуйте еще раз")
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
    while True:
        user_status_input = input()
        if user_status_input.upper() == "EXECUTED":
            print("Операции отфильтрованы по статусу \"EXECUTED\"")
        elif user_status_input.upper() == "CANCELED":
            print("Операции отфильтрованы по статусу \"CANCELED\"")
        elif user_status_input.upper() == "PENDING":
            print("Операции отфильтрованы по статусу \"PENDING\"")
        else:
             print(f"Статус операции \"{user_status_input}\" недоступен.")


print(main())
