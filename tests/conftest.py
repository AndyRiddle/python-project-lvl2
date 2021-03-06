import pytest


@pytest.fixture
def changes_betwen_flat_files_stylish():
    with open(
        'tests/fixtures/correct_flat_diff_stylish.txt',
    ) as correct_diff:
        return correct_diff.read()


@pytest.fixture
def changes_betwen_flat_files_plain():
    with open(
        'tests/fixtures/correct_flat_diff_plain.txt',
    ) as correct_diff:
        return correct_diff.read()


@pytest.fixture
def changes_betwen_flat_files_json():
    with open(
        'tests/fixtures/correct_flat_diff_json.txt',
    ) as correct_diff:
        return correct_diff.read()


@pytest.fixture
def changes_betwen_files_stylish():
    with open('tests/fixtures/correct_diff_stylish.txt') as correct_diff:
        return correct_diff.read()


@pytest.fixture
def changes_betwen_files_plain():
    with open('tests/fixtures/correct_diff_plain.txt') as correct_diff:
        return correct_diff.read()


@pytest.fixture
def changes_betwen_files_json():
    with open('tests/fixtures/correct_diff_json.txt') as correct_diff:
        return correct_diff.read()
