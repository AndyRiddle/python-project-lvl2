def format_value(value_for_output):
    if value_for_output is None:
        value_for_output = 'null'
    elif isinstance(value_for_output, bool):
        value_for_output = str(value_for_output)
        value_for_output = value_for_output.lower()
    elif isinstance(value_for_output, str):
        value_for_output = "'{0}'".format(value_for_output)
    return value_for_output


def get_values(changes, operation):
    if isinstance(changes[operation], (list, tuple, dict, set)):
        return '[complex value]'
    return format_value(changes[operation])


def generate_lines_for_output(changes, key, path):

    if ' ' in changes.keys():
        return None

    if '+' in changes.keys():
        added_value = get_values(changes, '+')
    else:
        return "Property '{0}' was removed".format(path)

    if '-' in changes.keys():
        removed_value = get_values(changes, '-')
    else:
        return "Property '{0}' was added with value: {1}".format(
            path,
            added_value,
        )

    return "Property '{0}' was updated. From {1} to {2}".format(
        path,
        removed_value,
        added_value,
    )


def generate_path_to_key(path, key):
    if path == '':
        return key
    return '.'.join([path, key])


def output_diff_plain(changes, recursively, path=''):
    for_output = []
    sorted_keys = sorted(recursively.keys())

    for key in sorted_keys:
        new_path = generate_path_to_key(path, key)
        if recursively[key]:
            for_output.append(output_diff_plain(
                changes[key],
                recursively[key],
                new_path,
            ))
        else:
            for_output.append(generate_lines_for_output(
                changes[key],
                key,
                new_path,
            ))

    return '\n'.join(filter(lambda line: line is not None, for_output))
