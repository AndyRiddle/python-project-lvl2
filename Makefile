install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	pytest

coverage:
	pytest --cov-report term --cov=tests

.PHONY: install lint test coverage