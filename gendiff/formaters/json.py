import json


def replacement_changes_line(recursively_changes):
    if '+' in recursively_changes.keys():
        recursively_changes['Value was added'] = recursively_changes.pop('+')

    if '-' in recursively_changes.keys():
        recursively_changes['Implication was removed'] = (
            recursively_changes.pop('-')
        )
    return recursively_changes


def gen_output_format(changes, recursively):
    for key, value_for_key in recursively.items():
        recursively_changes = changes[key]
        if value_for_key:
            gen_output_format(recursively_changes, value_for_key)
        else:
            recursively_changes = replacement_changes_line(recursively_changes)
        changes[key] = recursively_changes
    return changes, recursively


def output_diff_json(changes, recursively):

    gen_output_format(changes, recursively)

    return json.dumps(changes, indent=4, sort_keys=True)
