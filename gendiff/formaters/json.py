import json


def output_diff_json(changes):
    return json.dumps(changes, indent=4, sort_keys=True)
