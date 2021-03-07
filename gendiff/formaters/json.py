import json


def output_diff_json(changes, recursively):
    return json.dumps(changes, indent=4, sort_keys=True)
