import json


def get_data_from_json_file(path_to_file):
    with open(path_to_file) as data_of_file:
        return json.load(data_of_file)
