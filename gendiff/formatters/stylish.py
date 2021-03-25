import json

from gendiff.builder.search_differences import (ADDED_STATUS, CHANGED_STATUS,
                                                NEW_VALUE, OLD_VALUE,
                                                RECURSIVE_STATUS,
                                                REMOVED_STATUS,
                                                STATUS_PROPERTY,
                                                UNCHANGED_STATUS,
                                                VALUE_PROPERTY)

INDENT = '    '
ADDED = '+'
REMOVED = '-'


def format_diff_stylish(diff):
    return get_diff_stylish(diff)


def get_diff_stylish(diff, depth=1):
    diff_lines = ['{']
    sorted_keys = sorted(diff.keys())

    for key in sorted_keys:
        status = diff[key][STATUS_PROPERTY]
        value = diff[key][VALUE_PROPERTY]
        diff_lines.append(get_formated_line(
            status,
            value,
            key,
            depth,
        ))
    diff_lines.append('{0}{1}'.format(get_indent(depth - 1), '}'))
    return '\n'.join(diff_lines)


def get_formated_line(
    status,
    value,
    key,
    depth,
):
    depth_for_changed = depth - 1
    depth_for_unchanged = depth + 1
    if status == ADDED_STATUS:
        return get_line_for_changed_key(
            get_indent(depth_for_changed),
            ADDED,
            key,
            format_value(value, depth),
        )
    elif status == REMOVED_STATUS:
        return get_line_for_changed_key(
            get_indent(depth_for_changed),
            REMOVED,
            key,
            format_value(value, depth),
        )
    elif status == CHANGED_STATUS:
        return '{0}\n{1}'.format(
            get_line_for_changed_key(
                get_indent(depth_for_changed),
                REMOVED,
                key,
                format_value(
                    value[OLD_VALUE], depth,
                ),
            ),
            get_line_for_changed_key(
                get_indent(depth_for_changed),
                ADDED,
                key,
                format_value(
                    value[NEW_VALUE], depth,
                ),
            ),
        )
    elif status == RECURSIVE_STATUS:
        return get_line_for_unchanged_key(
            get_indent(depth),
            key,
            get_diff_stylish(
                value,
                depth_for_unchanged,
            ),
        )
    elif status == UNCHANGED_STATUS:
        return get_line_for_unchanged_key(
            get_indent(depth),
            key,
            format_value(
                value, depth_for_unchanged,
            ),
        )


def get_line_for_changed_key(indent, status, key, value_for_key):
    return '{0}  {1} {2}: {3}'.format(
        indent,
        status,
        key,
        value_for_key,
    )


def get_line_for_unchanged_key(indent, key, value_for_key):
    return '{0}{1}: {2}'.format(
        indent,
        key,
        value_for_key,
    )


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)
    return format_simple_value(value)


def format_dict(dictionary, depth):
    diff_lines = ['{']
    for key, value_for_key in dictionary.items():
        if isinstance(value_for_key, dict):
            diff_lines.append(get_line_for_unchanged_key(
                get_indent(depth + 1),
                key,
                format_dict(value_for_key, depth + 1),
            ))
        else:
            diff_lines.append(
                get_line_for_unchanged_key(
                    get_indent(depth + 1),
                    key,
                    format_simple_value(value_for_key),
                ),
            )
    diff_lines.append('{0}{1}'.format(get_indent(depth), '}'))
    return '\n'.join(diff_lines)


def format_simple_value(value):
    if isinstance(value, str):
        return '{0}'.format(value)
    return json.dumps(value)


def get_indent(depth):
    return INDENT * depth
