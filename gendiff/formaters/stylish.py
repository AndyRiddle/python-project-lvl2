import json

from gendiff.building_diff.search_differences import (  # isort:skip
    ADDED_STATUS,
    CHANGED_STATUS,
    NEW_VALUE,
    OLD_VALUE,
    RECURSIVE_STATUS,
    REMOVED_STATUS,
    STATUS_PROPERTY,
    UNCHANGED_STATUS,
    VALUE_PROPERTY,
)

INDENT = '    '


def format_value(value_for_output):
    if isinstance(value_for_output, str):
        return '{0}'.format(value_for_output)
    return json.dumps(value_for_output)


def genrate_lin_for_unchanged_key(indent, key, value_for_key):
    return '{0}{1}: {2}'.format(
        indent,
        key,
        value_for_key,
    )


def genrate_lin_for_changed_key(indent, status, key, value_for_key):
    return '{0}  {1} {2}: {3}'.format(
        indent,
        status,
        key,
        value_for_key,
    )


def output_unchanged_dict(dictionary, nesting_counter):
    format_for_output = ['{']
    for key, value_for_key in dictionary.items():
        if isinstance(value_for_key, dict):
            format_for_output.append(genrate_lin_for_unchanged_key(
                INDENT * (nesting_counter + 1),
                key,
                output_unchanged_dict(value_for_key, nesting_counter + 1),
            ))
        else:
            format_for_output.append(
                genrate_lin_for_unchanged_key(
                    INDENT * (nesting_counter + 1),
                    key,
                    format_value(value_for_key),
                ),
            )
    format_for_output.append('{0}{1}'.format(INDENT * nesting_counter, '}'))
    return '\n'.join(format_for_output)


def output_value(value_key, nesting_counter):
    if isinstance(value_key, dict):
        return output_unchanged_dict(value_key, nesting_counter)
    return format_value(value_key)


def generate_line_for_output(
    status_key,
    value_key,
    key,
    nesting_counter,
):
    nesting_counter_for_changed = nesting_counter - 1
    nesting_counter_for_unchanged = nesting_counter + 1
    if status_key == ADDED_STATUS:
        return genrate_lin_for_changed_key(
            INDENT * nesting_counter_for_changed,
            '+',
            key,
            output_value(value_key, nesting_counter),
        )
    elif status_key == REMOVED_STATUS:
        return genrate_lin_for_changed_key(
            INDENT * nesting_counter_for_changed,
            '-',
            key,
            output_value(value_key, nesting_counter),
        )
    elif status_key == CHANGED_STATUS:
        return '{0}\n{1}'.format(
            genrate_lin_for_changed_key(
                INDENT * nesting_counter_for_changed,
                '-',
                key,
                output_value(
                    value_key[OLD_VALUE], nesting_counter,
                ),
            ),
            genrate_lin_for_changed_key(
                INDENT * nesting_counter_for_changed,
                '+',
                key,
                output_value(
                    value_key[NEW_VALUE], nesting_counter_for_unchanged,
                ),
            ),
        )
    elif status_key == RECURSIVE_STATUS:
        return genrate_lin_for_unchanged_key(
            INDENT * nesting_counter,
            key,
            output_diff_stylish(
                value_key, nesting_counter_for_unchanged,
            ),
        )
    elif status_key == UNCHANGED_STATUS:
        return genrate_lin_for_unchanged_key(
            INDENT * nesting_counter,
            key,
            output_value(
                value_key, nesting_counter_for_unchanged,
            ),
        )


def output_diff_stylish(changes, nesting_counter=1):
    for_output = ['{']
    sorted_keys = sorted(changes.keys())

    for key in sorted_keys:
        status_key = changes[key].get(STATUS_PROPERTY)
        value_key = changes[key].get(VALUE_PROPERTY)
        if status_key is not None and value_key is not None:
            for_output.append(generate_line_for_output(
                status_key,
                value_key,
                key,
                nesting_counter,
            ))
    for_output.append('{0}{1}'.format((INDENT * (nesting_counter - 1)), '}'))
    return '\n'.join(for_output)
