ADDED_STATUS = 'added'
REMOVED_STATUS = 'removed'
CHANGED_STATUS = 'changed'
UNCHANGED_STATUS = 'unchanged'
RECURSIVE_STATUS = 'recursive'
STATUS_PROPERTY = 'status_of_key'
VALUE_PROPERTY = 'value_of_key'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'


def determine_differences(data_of_file1, data_of_file2):
    if data_of_file1 == data_of_file2:
        return {
            STATUS_PROPERTY: UNCHANGED_STATUS,
            VALUE_PROPERTY: data_of_file1,
        }
    elif isinstance(data_of_file1, dict) and isinstance(data_of_file2, dict):
        return {
            STATUS_PROPERTY: RECURSIVE_STATUS,
            VALUE_PROPERTY: build_diff(data_of_file1, data_of_file2),
        }
    return {
        STATUS_PROPERTY: CHANGED_STATUS,
        VALUE_PROPERTY: {
            OLD_VALUE: data_of_file1,
            NEW_VALUE: data_of_file2,
        },
    }


def build_diff(data_of_file1, data_of_file2):
    changes = {}
    all_keys = data_of_file1.keys() | data_of_file2.keys()

    for key in all_keys:
        if key not in data_of_file2:
            value_for_key = {
                STATUS_PROPERTY: REMOVED_STATUS,
                VALUE_PROPERTY: data_of_file1[key],
            }
        elif key not in data_of_file1:
            value_for_key = {
                STATUS_PROPERTY: ADDED_STATUS,
                VALUE_PROPERTY: data_of_file2[key],
            }
        else:
            value_for_key = determine_differences(
                data_of_file1[key],
                data_of_file2[key],
            )

        changes[key] = value_for_key

    return changes
