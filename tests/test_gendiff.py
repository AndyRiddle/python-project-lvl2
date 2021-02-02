import pytest

from gendiff import generate_diff


@pytest.fixture
def changes_betwen_flat_files():
    with open('tests/fixtures/flat_json_file.txt') as correct_diff:
        return correct_diff.read()


def test_compare_flat_json(changes_betwen_flat_files):  # noqa: WPS442
    assert generate_diff(  # noqa: S101
        'tests/fixtures/flat_file1.json',
        'tests/fixtures/flat_file2.json',
    ) == changes_betwen_flat_files
