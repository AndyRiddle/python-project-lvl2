INDENT = '    '


def format_value(value_for_output):
    if value_for_output is None:
        value_for_output = 'null'
    elif isinstance(value_for_output, bool):
        value_for_output = str(value_for_output)
        value_for_output = value_for_output.lower()

    return value_for_output


def output_unchanged_dict(dictionary, counter):
    style_for_output = ['{']
    for key, value_for_key in dictionary.items():
        if isinstance(value_for_key, dict):
            style_for_output.append('{0}{1}: {2}'.format(
                INDENT * (counter + 1),
                key,
                output_unchanged_dict(value_for_key, counter + 1),
            ))
        else:
            style_for_output.append('{0}{1}: {2}'.format(
                INDENT * (counter + 1), key, format_value(value_for_key),
            ))
    style_for_output.append(''.join([INDENT * counter, '}']))
    return '\n'.join(style_for_output)


def generate_changes_for_output(changes, key, counter):
    for_output = []
    for operation, value_for_key in changes.items():
        if isinstance(value_for_key, dict):
            for_output.append('{0}  {1} {2}: {3}'.format(
                INDENT * (counter - 1),
                operation,
                key,
                output_unchanged_dict(value_for_key, counter),
            ))
        else:
            for_output.append('{0}  {1} {2}: {3}'.format(
                INDENT * (counter - 1),
                operation,
                key,
                format_value(value_for_key),
            ))
    return '\n'.join(for_output)


def output_diff(changes, recursively, counter=1):
    for_output = ['{']
    sorted_keys = sorted(recursively.keys())

    for key in sorted_keys:
        if recursively[key]:
            for_output.append('{0}{1}: {2}'.format(
                INDENT * counter, key, output_diff(
                    changes[key], recursively[key], counter + 1,
                ),
            ))
        else:
            for_output.append(generate_changes_for_output(
                changes[key], key, counter,
            ))

    for_output.append(''.join([INDENT * (counter - 1), '}']))
    return '\n'.join(for_output)
