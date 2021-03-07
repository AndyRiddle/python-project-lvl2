import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    "file_with_correct_diff,old_file,new_file,output_format",
    [
        ('tests/fixtures/correct_diff_json.txt',
         'tests/fixtures/file_old.yaml',
         'tests/fixtures/file_new.yaml',
         'json',
         ),
        ('tests/fixtures/correct_diff_json.txt',
         'tests/fixtures/file_old.json',
         'tests/fixtures/file_new.json',
         'json',
         ),
        ('tests/fixtures/correct_flat_diff_json.txt',
         'tests/fixtures/flat_file_old.yaml',
         'tests/fixtures/flat_file_new.yaml',
         'json',
         ),
        ('tests/fixtures/correct_flat_diff_json.txt',
         'tests/fixtures/flat_file_old.json',
         'tests/fixtures/flat_file_new.json',
         'json',
         ),
        ('tests/fixtures/correct_diff_plain.txt',
         'tests/fixtures/file_old.yaml',
         'tests/fixtures/file_new.yaml',
         'plain',
         ),
        ('tests/fixtures/correct_diff_plain.txt',
         'tests/fixtures/file_old.json',
         'tests/fixtures/file_new.json',
         'plain',
         ),
        ('tests/fixtures/correct_flat_diff_plain.txt',
         'tests/fixtures/flat_file_old.yaml',
         'tests/fixtures/flat_file_new.yaml',
         'plain',
         ),
        ('tests/fixtures/correct_flat_diff_stylish.txt',
         'tests/fixtures/flat_file_old.json',
         'tests/fixtures/flat_file_new.json',
         'stylish',
         ),
        ('tests/fixtures/correct_diff_stylish.txt',
         'tests/fixtures/file_old.yaml',
         'tests/fixtures/file_new.yaml',
         'stylish',
         ),
        ('tests/fixtures/correct_diff_stylish.txt',
         'tests/fixtures/file_old.json',
         'tests/fixtures/file_new.json',
         'stylish',
         ),
        ('tests/fixtures/correct_flat_diff_stylish.txt',
         'tests/fixtures/flat_file_old.yaml',
         'tests/fixtures/flat_file_new.yaml',
         'stylish',
         ),
        ('tests/fixtures/correct_flat_diff_stylish.txt',
         'tests/fixtures/flat_file_old.json',
         'tests/fixtures/flat_file_new.json',
         'stylish',
         ),
    ],
)
def test_gendiff(file_with_correct_diff, old_file, new_file, output_format):
    with open(
        file_with_correct_diff,
    ) as correct_data:
        correct_diff = correct_data.read()
    assert generate_diff(
        old_file,
        new_file,
        output_format,
    ) == correct_diff
