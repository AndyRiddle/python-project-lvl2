import json
import os

import yaml


def get_file_data(path):

    loader_formats = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }

    file_extension = get_file_extension(path)

    with open(path) as open_file:
        format_file = loader_formats.get(file_extension)
        if format_file is None:
            raise ValueError("Invalid file format: '{0}'".format(path))
        file_data = format_file(open_file)

    return file_data


def get_file_extension(path):
    _, extension = os.path.splitext(path)
    return extension.lower()
