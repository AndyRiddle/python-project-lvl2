import os


def determine_type_of_file(path):
    split_path = os.path.splitext(path)
    return split_path[1]
