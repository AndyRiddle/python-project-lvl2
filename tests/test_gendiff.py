import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    "file_with_correct_diff,old_file,new_file,output_format",
    [
        ('correct_diff_json.txt',
         'file_old.yaml',
         'file_new.yaml',
         'json',
         ),
        ('correct_diff_json.txt',
         'file_old.json',
         'file_new.json',
         'json',
         ),
        ('correct_flat_diff_json.txt',
         'flat_file_old.yaml',
         'flat_file_new.yaml',
         'json',
         ),
        ('correct_flat_diff_json.txt',
         'flat_file_old.json',
         'flat_file_new.json',
         'json',
         ),
        ('correct_diff_plain.txt',
         'file_old.yaml',
         'file_new.yaml',
         'plain',
         ),
        ('correct_diff_plain.txt',
         'file_old.json',
         'file_new.json',
         'plain',
         ),
        ('correct_flat_diff_plain.txt',
         'flat_file_old.yaml',
         'flat_file_new.yaml',
         'plain',
         ),
        ('correct_flat_diff_plain.txt',
         'flat_file_old.json',
         'flat_file_new.json',
         'plain',
         ),
        ('correct_diff_stylish.txt',
         'file_old.yaml',
         'file_new.yaml',
         'stylish',
         ),
        ('correct_diff_stylish.txt',
         'file_old.json',
         'file_new.json',
         'stylish',
         ),
        ('correct_flat_diff_stylish.txt',
         'flat_file_old.yaml',
         'flat_file_new.yaml',
         'stylish',
         ),
        ('correct_flat_diff_stylish.txt',
         'flat_file_old.json',
         'flat_file_new.json',
         'stylish',
         ),
    ],
)
def test_for_gendiff(
    file_with_correct_diff,
    old_file,
    new_file,
    output_format,
):
    file_with_correct_diff = gen_file_path(file_with_correct_diff)
    old_file = gen_file_path(old_file)
    new_file = gen_file_path(new_file)
    with open(
        file_with_correct_diff,
    ) as correct_data:
        correct_diff = correct_data.read()
    assert generate_diff(
        old_file,
        new_file,
        output_format,
    ) == correct_diff


@pytest.mark.parametrize(
    "file_with_correct_diff,old_file,new_file",
    [
        ('correct_diff_stylish.txt',
         'file_old.yaml',
         'file_new.yaml',
         ),
        ('correct_diff_stylish.txt',
         'file_old.json',
         'file_new.json',
         ),
        ('correct_flat_diff_stylish.txt',
         'flat_file_old.yaml',
         'flat_file_new.yaml',
         ),
        ('correct_flat_diff_stylish.txt',
         'flat_file_old.json',
         'flat_file_new.json',
         ),
    ],
)
def test_for_gendiff_default_format(
    file_with_correct_diff,
    old_file,
    new_file,
):
    file_with_correct_diff = gen_file_path(file_with_correct_diff)
    old_file = gen_file_path(old_file)
    new_file = gen_file_path(new_file)
    with open(
        file_with_correct_diff,
    ) as correct_data:
        correct_diff = correct_data.read()
    assert generate_diff(
        old_file,
        new_file,
    ) == correct_diff


def gen_file_path(file_name):
    return 'tests/fixtures/{0}'.format(file_name)
