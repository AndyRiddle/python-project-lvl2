import json

import yaml


def get_data_from_file(path_to_file, type_of_file):
    if type_of_file == 'json':
        with open(path_to_file) as content_of_json_file:
            data_of_file = json.load(content_of_json_file)
    else:
        with open(path_to_file) as content_of_yaml_file:
            data_of_file = yaml.safe_load(content_of_yaml_file)

    for key, value_of_key in data_of_file.items():
        if isinstance(value_of_key, bool):
            value_of_key = str(value_of_key)
            data_of_file[key] = value_of_key.lower()
    return data_of_file
