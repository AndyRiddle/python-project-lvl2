from gendiff.formaters.json import output_diff_json
from gendiff.formaters.plain import output_diff_plain
from gendiff.formaters.stylish import output_diff_stylish


def identify_formater_and_output(
    formater,
    file_changes,
):
    output_of_formaters = {
        'stylish': output_diff_stylish,
        'plain': output_diff_plain,
        'json': output_diff_json,
    }

    output_formater = output_of_formaters.get(formater)
    if output_formater is None:
        raise ValueError("Unknown format name: '{0}'".format(formater))
    return output_formater(file_changes)
