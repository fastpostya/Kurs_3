import pytest
import config
import datetime
from utils.functions import get_path_from_config, open_json_file, change_date, get_only_executed, hide_digit, print_dict

def test_get_path_from_config(path_file):
    assert get_path_from_config( ) == r"data\operations.json"

def test_open_json_file(test_json, path_wrong):
    assert open_json_file(r"..\test\test_json.json") == test_json
    assert open_json_file(path_wrong) is None

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

def test_sort_dict_by_date(list_dict_for_sorting, test_json_sort):
    assert test_sort_dict_by_date(test_json_sort) == [
    {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2012-05-04T08:21:33.419441"
    },
    {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
    },
    {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441"
    }
    ]






    # assert test_sort_dict_by_date(list_dict_for_sorting) == [
    #     {"key1": "1238941", "date": "2022-12-01"},
    #     {"key1": "123", "date": "2018-12-13"},
    #     {"key1": "1238956", "date": "2019-12-01"}]

def test_hide_digit():
    assert hide_digit("Счет 59986621134048778289") == "Счет **8289"
    assert hide_digit("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"
    assert hide_digit("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert hide_digit("MasterCard") == "MasterCard"

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

# def test_print_dict(test_json_status):
#     assert print_dict(test_json_status, 2) == """26-08-2019 Перевод организации
#     Maestro 1596 83** **** 5199 -> Счет **9589
#     31957.58 руб
#
#     14-10-2018 Перевод с карты на счет
#     Maestro 3928 54** **** 4026 -> Счет **3493
#     77751.04 руб."""
#     assert print_dict(test_json_status, 5)is None
#     assert print_dict([], 2) is None
