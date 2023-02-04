import os
import config
import json
import datetime
import requests

def get_path_from_config()->str:
    """
    Загружает путь к файлу c JSON из файла config.py
    :return: путь к файлу в формате str
    """
    path = config.path_file_json
    return os.path.sep.join(path)

def open_json(path)->list:
    """
    Загружает JSON по URL, указанному в переменной path
    :param path: путь к JSON
    :return: путь к файлу в формате JSON
    """
    try:
        response = requests.get(path)
        if response.status_code == 200:
            return response.json()
    except requests.exception.ConnectionError():
        return None
    except requests.exception.JSONDecodeError():
        return None


def open_json_file(path)->list:
    """
    Функция читает данные из файла, путь к которому  указан в переменной path и возвращает их в формте JSON
    :param path: путь к JSON
    :return: путь к файлу в формате JSON
    """
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding="utf-8") as file:
                file_json = file.read()
                dict = json.loads(file_json)
                return dict
    except:
        print("Ошибка открытия файла")

def sort_dict_by_date(dict_list)->list:
    """
    Функция  сортирует список словарей по ключу date
    :param dict_list: исходный список словарей
    :return: отсортированный список словарей
    """
    dict_list_sorted = sorted(dict_list, key=lambda x: x['date'], reverse=True)
    return dict_list_sorted

def get_only_executed(dict_list)->list:
    """
    Функция возвращает из исходного списка только те значения словарей, у  которых ключ state равен EXECUTED
    :param dict_list: исходный список словарей
    :return: отфильтрованный список словарей
    """
    for dic in dict_list:
        if (not 'state' in dic) or dic['state'].upper() != 'EXECUTED':
            dict_list.remove(dic)
    return dict_list

def hide_digit(text)->str:
    """
    Функция заменяет цифры в номере счета и карты на *.
    - Номер карты отображается в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по
    блокам по 4 цифры, разделенных пробелом)
    - Номер счета отображается  в формате  **XXXX (видны только последние 4 цифры номера счета)
    :param text: исходный текст
    :return: текст со скрытыми цифрами
    """
    if len(text) < 20:
        return text
    elif text[0:4] == "Счет":
        return text[0:5] + "**"  + text[-4:]
    else:
        return text[0:len(text) - 12] + " " + text[len(text) - 12:len(text) - 10] + "** **** " + text[-4:]

def print_dict(dict_list, number):
    """
    Функция формирует текст для вывода заданного числа словарей из списка dict_list. Число позиций задается в переменной number.
    :param dict_list: исходный список словарей в формате JSONн
    :param number: число позиций списка, которое будет выведено
    :return: текст для вывода на печать
    """
    text =""
    if number <= len(dict_list):
        for i in range(0, number):
            dic = dict_list[i]
            text += datetime.date.fromisoformat(dic["date"][0:10]).strftime('%d-%m-%Y') + " "
            text += dic['description'] + '\n'
            if 'from' in dic:
                text += hide_digit(dic['from'])
            if 'to' in dic:
                text += " -> " + hide_digit(dic['to'])
            text += "\n"
            text += dic['operationAmount']['amount'] + " "
            text +=dic['operationAmount']['currency']['name']
            text += "\n\n"
    return text

