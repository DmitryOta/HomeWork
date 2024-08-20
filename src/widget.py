from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(cards_accounts: str) -> str:
    """Функция принимает номер карты или счета и возвращает их маску"""
    mask_cards_account = []
    split_cards_accounts = cards_accounts.split()
    for velue in split_cards_accounts:
        if velue.isalpha():
            mask_cards_account.append(velue)
        if velue.isdigit() and len(velue) == 16:
            mask_cards_account.append(get_mask_card_number(velue))
        if velue.isdigit() and len(velue) > 16:
            mask_cards_account.append(get_mask_account(velue))
    return " ".join(mask_cards_account)


def get_date(date: str) -> str:
    """Функция принемает дату и возвращает ее в формате ДД.ММ.ГГГГ"""
    reverse_date = ".".join(date[:10].split("-")[::-1])
    return reverse_date
