import json

from gendiff.building_diff.search_differences import (ADDED_STATUS,
                                                      CHANGED_STATUS,
                                                      NEW_VALUE, OLD_VALUE,
                                                      RECURSIVE_STATUS,
                                                      REMOVED_STATUS,
                                                      STATUS_PROPERTY,
                                                      UNCHANGED_STATUS,
                                                      VALUE_PROPERTY)


def get_values(value_for_key):
    if isinstance(value_for_key, (list, tuple, dict, set)):
        return '[complex value]'
    elif isinstance(value_for_key, str):
        return "'{0}'".format(value_for_key)
    return json.dumps(value_for_key)


def generate_path_to_key(path, key):
    if path == '':
        return key
    return '{0}.{1}'.format(path, key)


def generate_line_for_output(status_key, value_key, new_path):
    if status_key == ADDED_STATUS:
        return "Property '{0}' was added with value: {1}".format(
            new_path,
            get_values(value_key),
        )
    elif status_key == REMOVED_STATUS:
        return "Property '{0}' was removed".format(new_path)
    elif status_key == CHANGED_STATUS:
        return "Property '{0}' was updated. From {1} to {2}".format(
            new_path,
            get_values(value_key[OLD_VALUE]),
            get_values(value_key[NEW_VALUE]),
        )
    elif status_key == RECURSIVE_STATUS:
        return output_diff_plain(value_key, new_path)


def output_diff_plain(changes, path=''):
    for_output = []
    sorted_keys = sorted(changes.keys())

    for key in sorted_keys:
        status_key = changes[key].get(STATUS_PROPERTY)
        value_key = changes[key].get(VALUE_PROPERTY)
        if status_key is not None and value_key is not None:
            if status_key != UNCHANGED_STATUS:
                for_output.append(generate_line_for_output(
                    status_key,
                    value_key,
                    generate_path_to_key(path, key),
                ))

    return '\n'.join(for_output)
