import json

import yaml


def parse_data(data_format, received_data):
    formats = {
        'json': json.load,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load,
    }
    parse_received_data = formats.get(data_format)
    if parse_received_data is None:
        raise ValueError("Invalid format: '{0}'".format(data_format))
    return parse_received_data(received_data)
