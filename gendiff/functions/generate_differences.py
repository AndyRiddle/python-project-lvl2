from gendiff.formaters.plain import output_diff_plain
from gendiff.formaters.stylish import output_diff_stylish
from gendiff.functions.determine_file_type import determine_type_of_file
from gendiff.functions.open_file import get_data_from_file
from gendiff.functions.search_differences import identify_and_save_differences


def generate_diff(file1, file2, formater):

    data_of_file1 = get_data_from_file(
        file1,
        determine_type_of_file(file1),
    )
    data_of_file2 = get_data_from_file(
        file2,
        determine_type_of_file(file2),
    )

    file_changes, recursively = identify_and_save_differences(
        data_of_file1, data_of_file2,
    )

    if formater == 'stylish':
        return output_diff_stylish(file_changes, recursively)
    return output_diff_plain(file_changes, recursively)
