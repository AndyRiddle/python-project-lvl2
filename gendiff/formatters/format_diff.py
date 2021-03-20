from gendiff.formatters.json import format_diff_json
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.stylish import format_diff_stylish

JSON_FORMATTER = 'json'
PLAIN_FORMATTER = 'plain'
STYLISH_FORMATTER = 'stylish'


def format_diff(
    result_format,
    diff,
):
    output_formats = {
        STYLISH_FORMATTER: format_diff_stylish,
        PLAIN_FORMATTER: format_diff_plain,
        JSON_FORMATTER: format_diff_json,
    }

    formatter = output_formats.get(result_format)
    if formatter is None:
        raise ValueError("Unknown format name: '{0}'".format(result_format))
    return formatter(diff)
