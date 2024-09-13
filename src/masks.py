import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number: str) -> str:
    """Функия принимает номер карты и возврвщает ее маску"""
    logging.info("Начало работы функции")
    if number.isdigit:
        mask_number = number[:6] + ("*" * 6) + number[-4:]
        split_mask_number = ""
        logging.info("Скрытие номера")
        for i, num in enumerate(mask_number):
            if i == 4 or i == 8 or i == 12:
                split_mask_number += " " + num
            else:
                split_mask_number += num
    else:
        logging.error("неверный номер")
        return "В номере присутстуют буквы"
    logging.info("Окончание работы функции")
    return split_mask_number


def get_mask_account(account_num: str) -> str:
    """Функция возвращает маску для счета"""
    logging.info("Начало работы функции")
    mask_account = "**" + account_num[-4:]
    logging.info("Окончание работы функции")
    return mask_account
