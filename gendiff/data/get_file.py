import os

from gendiff.data.parse import parse_data


def get_file_data(path):

    file_extension = get_file_extension(path)

    with open(path) as open_file:
        return parse_data(file_extension, open_file)


def get_file_extension(path):
    _, extension = os.path.splitext(path)
    return extension.lower().lstrip('.')
