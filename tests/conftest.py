import pytest


@pytest.fixture
def changes_betwen_flat_files():
    with open('tests/fixtures/correct_flat_diff.txt') as correct_flat_diff:
        return correct_flat_diff.read()


@pytest.fixture
def changes_betwen_files():
    with open('tests/fixtures/correct_diff.txt') as correct_diff:
        return correct_diff.read()
