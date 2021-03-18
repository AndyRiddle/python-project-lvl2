ADDED_STATUS = 'added'
REMOVED_STATUS = 'removed'
CHANGED_STATUS = 'changed'
UNCHANGED_STATUS = 'unchanged'
RECURSIVE_STATUS = 'recursive'
STATUS_PROPERTY = 'status'
VALUE_PROPERTY = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'


def build_diff(dictionary1, dictionary2):
    diff = {}
    all_keys = dictionary1.keys() | dictionary2.keys()

    for key in all_keys:
        if key not in dictionary2:
            value_for_key = {
                STATUS_PROPERTY: REMOVED_STATUS,
                VALUE_PROPERTY: dictionary1[key],
            }
        elif key not in dictionary1:
            value_for_key = {
                STATUS_PROPERTY: ADDED_STATUS,
                VALUE_PROPERTY: dictionary2[key],
            }
        else:
            value_for_key = compare(
                dictionary1[key],
                dictionary2[key],
            )

        diff[key] = value_for_key

    return diff


def compare(dictionary1, dictionary2):
    if dictionary1 == dictionary2:
        return {
            STATUS_PROPERTY: UNCHANGED_STATUS,
            VALUE_PROPERTY: dictionary1,
        }
    elif isinstance(dictionary1, dict) and isinstance(dictionary2, dict):
        return {
            STATUS_PROPERTY: RECURSIVE_STATUS,
            VALUE_PROPERTY: build_diff(dictionary1, dictionary2),
        }
    return {
        STATUS_PROPERTY: CHANGED_STATUS,
        VALUE_PROPERTY: {
            OLD_VALUE: dictionary1,
            NEW_VALUE: dictionary2,
        },
    }
