install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	pytest

.PHONY: install lint test