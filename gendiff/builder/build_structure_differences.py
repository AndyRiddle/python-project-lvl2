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
        dictionary1_value = dictionary1.get(key)
        dictionary2_value = dictionary2.get(key)
        if key not in dictionary2:
            key_properties = {
                STATUS_PROPERTY: REMOVED_STATUS,
                VALUE_PROPERTY: dictionary1_value,
            }
        elif key not in dictionary1:
            key_properties = {
                STATUS_PROPERTY: ADDED_STATUS,
                VALUE_PROPERTY: dictionary2_value,
            }
        elif dictionary1_value == dictionary2_value:
            key_properties = {
                STATUS_PROPERTY: UNCHANGED_STATUS,
                VALUE_PROPERTY: dictionary1_value,
            }
        elif isinstance(dictionary1_value, dict) and isinstance(dictionary2_value, dict):
            key_properties = {
                STATUS_PROPERTY: RECURSIVE_STATUS,
                VALUE_PROPERTY: build_diff(
                    dictionary1_value,
                    dictionary2_value,
                ),
            }
        else:
            key_properties = {
                STATUS_PROPERTY: CHANGED_STATUS,
                VALUE_PROPERTY: {
                    OLD_VALUE: dictionary1_value,
                    NEW_VALUE: dictionary2_value,
                },
            }

        diff[key] = key_properties

    return diff
