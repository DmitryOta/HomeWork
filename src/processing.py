def filter_by_state(list_dict: list, state='EXECUTED') -> list:
    """ Функция возвращает отсортированый список словарей по ключю 'state' """
    new_list = []
    for i in list_dict:
        if i["state"] == state:
            new_list.append(i)
    return new_list
