import json

import yaml


def get_data_from_file(path_to_file, type_of_file):

    with open(path_to_file) as content_of_file:
        if type_of_file == 'json':
            data_of_file = json.load(content_of_file)
        else:
            data_of_file = yaml.safe_load(content_of_file)

    return data_of_file
