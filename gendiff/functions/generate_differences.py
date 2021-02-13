from gendiff.functions.determine_file_type import determine_type_of_file
from gendiff.functions.open_file import get_data_from_file
from gendiff.functions.output_differences import output_diff
from gendiff.functions.search_differences import identify_and_save_differences


def generate_diff(file1, file2):

    data_of_file1 = get_data_from_file(
        file1,
        determine_type_of_file(file1),
    )
    data_of_file2 = get_data_from_file(
        file2,
        determine_type_of_file(file2),
    )

    file_changes = identify_and_save_differences(
        data_of_file1, data_of_file2,
    )

    return output_diff(file_changes)
