def get_mask_card_number(number: str) -> str:
    """Функия принимает номер карты и возврвщает ее маску"""
    mask_number = number[:6] + ("*" * 6) + number[-4:]
    split_mask_number = ""
    for i, num in enumerate(mask_number):
        if i == 4 or i == 8 or i == 12:
            split_mask_number += " " + num
        else:
            split_mask_number += num
    return split_mask_number


def get_mask_account(account_num: str) -> str:
    """Функция возвращает маску для счета"""
    mask_account = "**" + account_num[-4:]
    return mask_account
