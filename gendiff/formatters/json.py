import json


def format_diff_json(diff):
    return json.dumps(diff, indent=4, sort_keys=True)
