import os
from operator import itemgetter
from utils.functions import get_path_from_config, open_json_file, \
    change_date, sort_dict_by_date, get_only_executed, print_dict
from config import number_operation


def main():
    path = get_path_from_config()
    if path:
        dict = open_json_file(path)
        dict = get_only_executed(dict)
        dict = change_date(dict)

        #print("Исходный словарь:")
        #print(dict)
        # for dic in dict:
        #     print(dic)
        dict_sorted = sort_dict_by_date(dict)
        #dict_list_sorted = sorted(dict, key=itemgetter('date'))

        #key="date")
        print(print_dict(dict_sorted, number_operation))

if __name__ == "__main__":
    main()
