import json
import os

import yaml


def get_file_data(path):

    file_extension = get_file_extension(path)

    with open(path) as open_file:
        return pars_data(file_extension, open_file)


def pars_data(file_format, file_data):
    formats = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    pars_file_data = formats.get(file_format)
    if pars_file_data is None:
        raise ValueError("Invalid file format: '{0}'".format(file_format))
    return pars_file_data(file_data)


def get_file_extension(path):
    _, extension = os.path.splitext(path)
    return extension.lower()
