def output_diff(changes):
    for_output = ['{']
    sorted_keys = sorted(changes.keys())

    for key in sorted_keys:
        for operation, value_for_key in changes[key].items():
            for_output.append('  {0} {1}: {2}'.format(
                operation, key, value_for_key,
            ))
    for_output.append('}')
    return '\n'.join(for_output)
