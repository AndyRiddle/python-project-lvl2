from gendiff import generate_diff


def test_compare_flat_json_stylish(changes_betwen_flat_files_stylish):
    assert generate_diff(
        'tests/fixtures/flat_file_old.json',
        'tests/fixtures/flat_file_new.json',
        'stylish',
    ) == changes_betwen_flat_files_stylish


def test_compare_flat_yaml_stylish(changes_betwen_flat_files_stylish):
    assert generate_diff(
        'tests/fixtures/flat_file_old.yaml',
        'tests/fixtures/flat_file_new.yaml',
        'stylish',
    ) == changes_betwen_flat_files_stylish


def test_compare_json_stylish(changes_betwen_files_stylish):
    assert generate_diff(
        'tests/fixtures/file_old.json',
        'tests/fixtures/file_new.json',
        'stylish',
    ) == changes_betwen_files_stylish


def test_compare_yaml_stylish(changes_betwen_files_stylish):
    assert generate_diff(
        'tests/fixtures/file_old.yaml',
        'tests/fixtures/file_new.yaml',
        'stylish',
    ) == changes_betwen_files_stylish


def test_compare_flat_json_plain(changes_betwen_flat_files_plain):
    assert generate_diff(
        'tests/fixtures/flat_file_old.json',
        'tests/fixtures/flat_file_new.json',
        'plain',
    ) == changes_betwen_flat_files_plain


def test_compare_flat_yaml_plain(changes_betwen_flat_files_plain):
    assert generate_diff(
        'tests/fixtures/flat_file_old.yaml',
        'tests/fixtures/flat_file_new.yaml',
        'plain',
    ) == changes_betwen_flat_files_plain


def test_compare_json_plain(changes_betwen_files_plain):
    assert generate_diff(
        'tests/fixtures/file_old.json',
        'tests/fixtures/file_new.json',
        'plain',
    ) == changes_betwen_files_plain


def test_compare_yaml_plain(changes_betwen_files_plain):
    assert generate_diff(
        'tests/fixtures/file_old.yaml',
        'tests/fixtures/file_new.yaml',
        'plain',
    ) == changes_betwen_files_plain


def test_compare_flat_json_json(changes_betwen_flat_files_json):
    assert generate_diff(
        'tests/fixtures/flat_file_old.json',
        'tests/fixtures/flat_file_new.json',
        'json',
    ) == changes_betwen_flat_files_json


def test_compare_flat_yaml_json(changes_betwen_flat_files_json):
    assert generate_diff(
        'tests/fixtures/flat_file_old.yaml',
        'tests/fixtures/flat_file_new.yaml',
        'json',
    ) == changes_betwen_flat_files_json


def test_compare_json_json(changes_betwen_files_json):
    assert generate_diff(
        'tests/fixtures/file_old.json',
        'tests/fixtures/file_new.json',
        'json',
    ) == changes_betwen_files_json


def test_compare_yaml_json(changes_betwen_files_json):
    assert generate_diff(
        'tests/fixtures/file_old.yaml',
        'tests/fixtures/file_new.yaml',
        'json',
    ) == changes_betwen_files_json
