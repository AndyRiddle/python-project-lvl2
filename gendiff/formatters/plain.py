import json

from gendiff.builder.search_differences import (ADDED_STATUS, CHANGED_STATUS,
                                                NEW_VALUE, OLD_VALUE,
                                                RECURSIVE_STATUS,
                                                REMOVED_STATUS,
                                                STATUS_PROPERTY,
                                                VALUE_PROPERTY)


def format_diff_plain(diff):
    return get_diff_plain(diff)


def get_diff_plain(diff, path=''):
    diff_lines = []
    sorted_keys = sorted(diff.keys())

    for key in sorted_keys:
        status = diff[key][STATUS_PROPERTY]
        value = diff[key][VALUE_PROPERTY]
        if status == ADDED_STATUS:
            diff_lines.append(
                "Property '{0}' was added with value: {1}".format(
                    get_path_to_key(path, key),
                    get_value(value),
                ),
            )
        elif status == REMOVED_STATUS:
            diff_lines.append("Property '{0}' was removed".format(
                get_path_to_key(path, key)))
        elif status == CHANGED_STATUS:
            diff_lines.append(
                "Property '{0}' was updated. From {1} to {2}".format(
                    get_path_to_key(path, key),
                    get_value(value[OLD_VALUE]),
                    get_value(value[NEW_VALUE]),
                ),
            )
        elif status == RECURSIVE_STATUS:
            diff_lines.append(get_diff_plain(
                value, get_path_to_key(path, key),
            ))

    return '\n'.join(diff_lines)


def get_path_to_key(path, key):
    if path == '':
        return key
    return '{0}.{1}'.format(path, key)


def get_value(value):
    if isinstance(value, (list, tuple, dict, set)):
        return '[complex value]'
    elif isinstance(value, str):
        return "'{0}'".format(value)
    return json.dumps(value)
