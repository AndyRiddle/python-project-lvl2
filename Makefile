install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

coverage:
	poetry run pytest --cov-report term --cov=gendiff

.PHONY: install lint test coverage