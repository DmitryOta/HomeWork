def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает отсортированый список словарей по ключю 'state'"""
    new_list = []
    for i in list_dict:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list, sorting: bool = True) -> list:
    """Функция водвращает отсортированый список словарей, отсортированный по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=sorting)
    return sorted_list
