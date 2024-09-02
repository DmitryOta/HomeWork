# Виджет для банка
## Описание
Этот виджет позволяет выполнять несколько задач для работы с банковскими счетоми и картами, а также финансовыми операциями клиентов.

## Статус:
В разработке



## На данный момент реализован следующий функционал:
- Модуль **masks.py** со следующими функциями:
- *get_mask_card_number* - маскирует номер карты по шаблону
- *get_mask_account* - маскирует номер счета по шаблону
- Модуль **widget.py** со следующими функциями:
- *mask_account_card* - используя функции из masks.py возвращает замаскированный номер счета либо карты
- *get_date* - форматирует строку с датой, возвращая дату формата ДД.ММ.ГГГГ
- Модуль **processing.py** со следующими функциями:
- *filter_by_state* - фильтрует банкцовские операции по их состоянию
- *sort_by_date* - сортирует банковские операции по дате
- Модуль **generators.py** со следующими функциями:
- *filter_by_currency* - поочередно выдает транзакции, где валюта операции USD
- *transaction_description* - возвращает описание каждой операции
- *card_number_generator* - генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX
    , где X — цифра номера карты
- Модуль **decorators.py** со следующими функциями:
- *log* - Функция декоратор которая логирует начало и конец выполнения функции,
     а также ее результаты или возникшие ошибки.
- Модуль **external_api.py** со следующими функциями:
- *get_amount_transaction* - Функция возвращает сумму транзакции в рублях если транзакция была в другой валюте функция переведет в рубли
- Модуль **utils.py** со следующими функциями:
- *unpacking_json* - Функция, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
## Логирование проекта:
### Все логи храняться в папке *logs* 
- Добавлено логирование двух модулей: **utils.py** и **masks.py**. Фориат логирования (время, название модуля, уровень серьезности и сообщение, описывающее событие или ошибку.)
## Структура проекта:
- Проект использует виртуальное окружение **Poetry**. Информация о зависимостях проекта находится в файле *pyproject.toml*.
- Для более простой установки зависимостей рекомендуется использовать виртуальное окружение **Poetry**.
- Чтобы установить зависимости используйте следующую команду:`poetry install`
## Информация о тестировании проекта:
- Проект использует pytest в качестве фреймворка для тестирования. Для каждого модуля создан отдельный unit-тест с тем же названием.
- Информацию о тестировании можно найти в директории htmlcov в корне проекта.
- Для прогонки тестов используйте команду:`pytest`
Для отображения информации о покрытии проекта тестами используйте команду:`pytest --cov`
- На данный момент проект покрыт тестами на 100%. С будущими доработками тесты будут расширяться.
