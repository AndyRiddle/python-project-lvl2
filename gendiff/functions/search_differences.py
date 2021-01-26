def identify_and_save_differences(data_of_file1, data_of_file2):
    changes = {}
    all_keys = data_of_file1.keys() | data_of_file2.keys()

    for key in all_keys:
        if key not in data_of_file2:
            value_for_key = {'-': data_of_file1[key]}
        elif key not in data_of_file1:
            value_for_key = {'+': data_of_file2[key]}
        elif data_of_file1[key] == data_of_file2[key]:
            value_for_key = {' ': data_of_file1[key]}
        else:
            value_for_key = {'-': data_of_file1[key], '+': data_of_file2[key]}
        changes[key] = value_for_key
    return changes
