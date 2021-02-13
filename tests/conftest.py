import pytest


@pytest.fixture
def changes_betwen_flat_files():
    with open('tests/fixtures/flat_json_file.txt') as correct_diff:
        return correct_diff.read()
