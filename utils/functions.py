import os
import config
import json
import datetime
from operator import itemgetter

def get_path_from_config():
    path = config.path_json
    return os.path.sep.join(path)

def open_json_file(path):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding="utf-8") as file:
                file_json = file.read()
                text = json.loads(file_json)
                return text
    except:
        print("Ошибка открытия файла")

def change_date(list_dict):
    for dict_el in list_dict:
        if "date" in dict_el:
            dict_el["date"] = datetime.date(int(dict_el["date"][0:4]), int(dict_el["date"][5:7]), int(dict_el["date"][8:10]))
    return list_dict


def sort_dict_by_date(dict_list):
    dict_list_sorted = sorted(dict_list, key=itemgetter('date'), reverse=True)
    return dict_list_sorted

def get_only_executed(dict_list):
    for dic in dict_list:
        if (not 'state' in dic) or dic['state'].upper() != 'EXECUTED':
            dict_list.remove(dic)
    return dict_list


def print_dict(dict_list, number):
    text =""
    for i in range(0, number):
        dic = dict_list[i]
        text +=   str(dic["date"]) + " "
        text += dic['description'] + '\n'

        if 'from' in dic:
            text += dic['from']
        if 'to' in dic:
            text += " -> " + dic['to']
        text += "\n"
        text += dic['operationAmount']['amount'] + " "
        text +=dic['operationAmount']['currency']['name']
        text += "\n\n"
    return text


