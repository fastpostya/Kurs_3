import pytest

@pytest.fixture()
def path_file():
    return "data", "operations.json"

@pytest.fixture()
def path_wrong():
    return "data"

@pytest.fixture()
def test_json():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]

@pytest.fixture()
def test_json_status():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
      "amount": "77751.04",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 3928549031574026",
    "to": "Счет 84163357546688983493"
  }]

@pytest.fixture()
def list_dict_for_sorting():
    return [
    {"key1":"123", "date":"2018-12-13"},
    {"key1":"1238956", "date":"2019-12-01"},
    {"key1":"1238941", "date":"2022-12-01"}]

@pytest.fixture()
def test_json_sort():
    return [
    {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
    },
    {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441"
    },
    {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2012-05-04T08:21:33.419441"
    }
    ]