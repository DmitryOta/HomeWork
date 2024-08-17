import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_score, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_score, result):
    assert mask_account_card(card_score) == result


@pytest.mark.parametrize(
    "date, revers_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date(date, revers_date):
    assert get_date(date) == revers_date
