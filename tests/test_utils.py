import json
from unittest.mock import Mock

from src.utils import WEY_TO_FILE, unpacking_json


def test_unpacking_json():
    mock_unpacking = Mock(return_value=[{"name": "Dmitry", "age": 30, "profession": "Phyton"}])
    json.load = mock_unpacking
    assert unpacking_json(WEY_TO_FILE) == [{"name": "Dmitry", "age": 30, "profession": "Phyton"}]


def test_unpacking_json_empty():
    mock_unpacking = Mock(return_value=[])
    json.load = mock_unpacking
    assert unpacking_json(WEY_TO_FILE) == []
