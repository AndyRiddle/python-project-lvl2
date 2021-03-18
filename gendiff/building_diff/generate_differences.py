from gendiff.building_diff.get_file_data import get_file_data
from gendiff.building_diff.search_differences import build_diff
from gendiff.formatters.format_diff import format_diff


def generate_diff(file1, file2, formatter='stylish'):

    data_of_file1 = get_file_data(
        file1,
    )
    data_of_file2 = get_file_data(
        file2,
    )

    diff = build_diff(
        data_of_file1,
        data_of_file2,
    )

    return format_diff(
        formatter,
        diff,
    )
