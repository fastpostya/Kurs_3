from utils.functions import get_path_from_config, open_json_file, \
    sort_dict_by_date, get_only_executed, print_dict, open_json
from config import number_operation, url_json


def main():
    use_file = True
    if use_file:
        path = get_path_from_config()
        if path:
            dict = open_json_file(path)
    else:
        dict = open_json(url_json)
    dict = get_only_executed(dict)
    dict_sorted = sort_dict_by_date(dict)
    print(print_dict(dict_sorted, number_operation))

if __name__ == "__main__":
    main()
