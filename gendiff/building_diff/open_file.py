import json
import os

import yaml


def determine_type_of_file(path):
    split_path = os.path.splitext(path)
    return split_path[1].lower()


def get_data_from_file(path_to_file):

    loader_formats = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }

    type_of_file = determine_type_of_file(path_to_file)

    with open(path_to_file) as content_of_file:
        format_file = loader_formats.get(type_of_file)
        if format_file is None:
            raise ValueError("Invalid file format: '{0}'".format(path_to_file))
        data_of_file = format_file(content_of_file)

    return data_of_file
