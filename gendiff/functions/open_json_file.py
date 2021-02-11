import json


def get_data_from_json_file(path_to_file):
    with open(path_to_file) as content_of_file:
        data_of_file = json.load(content_of_file)

        for key, value_of_key in data_of_file.items():
            if isinstance(value_of_key, bool):
                value_of_key = str(value_of_key)
                data_of_file[key] = value_of_key.lower()
        return data_of_file
