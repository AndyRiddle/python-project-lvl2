from gendiff.building_diff.open_file import get_data_from_file
from gendiff.building_diff.search_differences import build_diff
from gendiff.formaters.identify_formater import identify_formater_and_output


def generate_diff(file1, file2, formater='stylish'):

    data_of_file1 = get_data_from_file(
        file1,
    )
    data_of_file2 = get_data_from_file(
        file2,
    )

    file_changes = build_diff(
        data_of_file1,
        data_of_file2,
    )

    return identify_formater_and_output(
        formater,
        file_changes,
    )
