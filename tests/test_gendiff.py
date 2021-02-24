from gendiff import generate_diff


def test_compare_flat_json(changes_betwen_flat_files):
    assert generate_diff(
        'tests/fixtures/flat_file_old.json',
        'tests/fixtures/flat_file_new.json',
        'stylish',
    ) == changes_betwen_flat_files


def test_compare_flat_yaml(changes_betwen_flat_files):
    assert generate_diff(
        'tests/fixtures/flat_file_old.yaml',
        'tests/fixtures/flat_file_new.yaml',
        'stylish',
    ) == changes_betwen_flat_files


def test_compare_json(changes_betwen_files):
    assert generate_diff(
        'tests/fixtures/file_old.yaml',
        'tests/fixtures/file_new.yaml',
        'stylish',
    ) == changes_betwen_files


def test_compare_yaml(changes_betwen_files):
    assert generate_diff(
        'tests/fixtures/file_old.yaml',
        'tests/fixtures/file_new.yaml',
        'stylish',
    ) == changes_betwen_files
