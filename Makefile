install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: install lint test coverage