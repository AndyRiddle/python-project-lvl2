def determine_differences(data_of_file1, data_of_file2):
    if data_of_file1 == data_of_file2:
        return {' ': data_of_file1}, {}
    elif isinstance(data_of_file1, dict) and isinstance(data_of_file2, dict):
        return identify_and_save_differences(
            data_of_file1,
            data_of_file2,
        )
    return {'-': data_of_file1, '+': data_of_file2}, {}


def identify_and_save_differences(data_of_file1, data_of_file2):
    changes = {}
    all_keys = data_of_file1.keys() | data_of_file2.keys()
    recursively = {}

    for key in all_keys:
        if key not in data_of_file2:
            value_for_key = {'-': data_of_file1[key]}
            for_recursively = {}
        elif key not in data_of_file1:
            value_for_key = {'+': data_of_file2[key]}
            for_recursively = {}
        else:
            value_for_key, for_recursively = determine_differences(
                data_of_file1[key],
                data_of_file2[key],
            )

        recursively[key] = for_recursively
        changes[key] = value_for_key

    return changes, recursively
