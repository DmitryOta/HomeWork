from unittest.mock import Mock, patch

from src.external_api import get_amount_transaction

transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
}


def test_get_amount_transaction():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 25, "from": "GBP", "to": "JPY"},
        "result": 3724.305775,
        "success": True,
    }

    with patch("requests.get", return_value=mock_response):
        result = get_amount_transaction(transaction)
        assert result == 3724.31


def test_get_amount_transaction_empty():
    assert get_amount_transaction({}) == False


def test_get_amount_transaction_error():
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 25, "from": "GBP", "to": "JPY"},
        "result": 3724.305775,
        "success": True,
    }

    with patch("requests.get", return_value=mock_response):
        result = get_amount_transaction(transaction)
        assert result == False
