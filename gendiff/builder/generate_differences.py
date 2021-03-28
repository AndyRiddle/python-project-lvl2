from gendiff.builder.build_structure_differences import build_diff
from gendiff.formatters.format_diff import format_diff
from gendiff.get_data.get_file_data import get_file_data


def generate_diff(file_path1, file_path2, output_format='stylish'):

    file1_data = get_file_data(
        file_path1,
    )
    file2_data = get_file_data(
        file_path2,
    )

    diff = build_diff(
        file1_data,
        file2_data,
    )

    return format_diff(
        output_format,
        diff,
    )
