import json

from gendiff.building_diff.search_differences import (ADDED_STATUS,
                                                      CHANGED_STATUS,
                                                      NEW_VALUE, OLD_VALUE,
                                                      RECURSIVE_STATUS,
                                                      REMOVED_STATUS,
                                                      STATUS_PROPERTY,
                                                      UNCHANGED_STATUS,
                                                      VALUE_PROPERTY)


def format_diff_plain(diff, path=''):
    diff_lines = []
    sorted_keys = sorted(diff.keys())

    for key in sorted_keys:
        status = diff[key][STATUS_PROPERTY]
        value = diff[key][VALUE_PROPERTY]
        if status != UNCHANGED_STATUS:
            diff_lines.append(get_formated_line(
                status,
                value,
                get_path_to_key(path, key),
            ))

    return '\n'.join(diff_lines)


def get_path_to_key(path, key):
    if path == '':
        return key
    return '{0}.{1}'.format(path, key)


def get_formated_line(status, value, path):
    if status == ADDED_STATUS:
        return "Property '{0}' was added with value: {1}".format(
            path,
            get_value(value),
        )
    elif status == REMOVED_STATUS:
        return "Property '{0}' was removed".format(path)
    elif status == CHANGED_STATUS:
        return "Property '{0}' was updated. From {1} to {2}".format(
            path,
            get_value(value[OLD_VALUE]),
            get_value(value[NEW_VALUE]),
        )
    elif status == RECURSIVE_STATUS:
        return format_diff_plain(value, path)


def get_value(value):
    if isinstance(value, (list, tuple, dict, set)):
        return '[complex value]'
    elif isinstance(value, str):
        return "'{0}'".format(value)
    return json.dumps(value)
