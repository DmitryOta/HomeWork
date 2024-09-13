import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, result",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_masks_card_number(number, result):
    assert get_mask_card_number(number) == result


@pytest.mark.parametrize(
    "score, result",
    [
        ("Счет 64686473678894779589", "**9589"),
        ("Счет 35383033474447895560", "**5560"),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(score, result):
    assert get_mask_account(score) == result
