import pytest
import config
import datetime
from utils.functions import get_path_from_config, open_json_file, change_date, get_only_executed

def test_get_path_from_config(path_file):
    assert get_path_from_config( ) == r"data\operations.json"


def test_open_json_file(test_json):
    assert open_json_file(r"..\test\test_json.json") == test_json
    #assert open_json_file(config.path_div.join(["test", "test_json.json"])) ==  test_json

def test_change_date(test_json):
    assert change_date([{"date": "2019-08-26hjhjtsssssssd"}]) == [{"date": datetime.date(2019, 8, 26)}]
    assert change_date(test_json) ==[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": datetime.date(2019, 8, 26),
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

def test_sort_dict_by_date(test_json_status):
    pass

def get_only_executed(test_json_status):
    assert get_only_executed([{"state": "EXECUTED"}, {"state": "NONE"}, {"amount": "31957.58"}]) == [{"state": "EXECUTED"}]
    assert get_only_executed([{'id': 27192367, 'state': 'CANCELED', 'date': '2018-12-24T20:16:18.819037',
     'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290', 'to': 'Счет 87448526688763159781'}]) == [{}]
    assert get_only_executed(test_json_status) == [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": datetime.date(2019, 8, 26),
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
