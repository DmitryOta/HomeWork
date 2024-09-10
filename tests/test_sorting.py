from src.sorting import count_categories, sorting_transactions


def test_count_categories(get_list_transaction, get_list_categories):
    assert count_categories(get_list_transaction, get_list_categories) == (
        {"Покупка продуктов в магазине 'Пятёрочка'": 1, "Оплата услуг ЖКХ": 1}
    )


def test_sorting_transactions(get_list_transaction, get_search_bar):
    assert sorting_transactions(get_list_transaction, get_search_bar) == ["Покупка продуктов в магазине 'Пятёрочка'"]
