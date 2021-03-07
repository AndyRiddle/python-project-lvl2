INDENT = '    '


def format_value(value_for_output):
    if value_for_output is None:
        value_for_output = 'null'
    elif isinstance(value_for_output, bool):
        value_for_output = str(value_for_output)
        value_for_output = value_for_output.lower()

    return value_for_output


def output_unchanged_dict(dictionary, nesting_counter):
    format_for_output = ['{']
    for key, value_for_key in dictionary.items():
        if isinstance(value_for_key, dict):
            format_for_output.append('{0}{1}: {2}'.format(
                INDENT * (nesting_counter + 1),
                key,
                output_unchanged_dict(value_for_key, nesting_counter + 1),
            ))
        else:
            format_for_output.append(
                '{0}{1}: {2}'.format(
                    INDENT * (nesting_counter + 1),
                    key,
                    format_value(value_for_key),
                ),
            )
    format_for_output.append(''.join([INDENT * nesting_counter, '}']))
    return '\n'.join(format_for_output)


def generate_changes_for_output(changes, key, nesting_counter):
    for_output = []
    for operation, value_for_key in changes.items():
        if isinstance(value_for_key, dict):
            for_output.append('{0}  {1} {2}: {3}'.format(
                INDENT * (nesting_counter - 1),
                operation,
                key,
                output_unchanged_dict(value_for_key, nesting_counter),
            ))
        else:
            for_output.append('{0}  {1} {2}: {3}'.format(
                INDENT * (nesting_counter - 1),
                operation,
                key,
                format_value(value_for_key),
            ))
    return '\n'.join(for_output)


def output_diff_stylish(changes, recursively, nesting_counter=1):
    for_output = ['{']
    sorted_keys = sorted(recursively.keys())

    for key in sorted_keys:
        if recursively[key]:
            for_output.append('{0}{1}: {2}'.format(
                INDENT * nesting_counter, key, output_diff_stylish(
                    changes[key], recursively[key], nesting_counter + 1,
                ),
            ))
        else:
            for_output.append(generate_changes_for_output(
                changes[key], key, nesting_counter,
            ))

    for_output.append(''.join([INDENT * (nesting_counter - 1), '}']))
    return '\n'.join(for_output)
