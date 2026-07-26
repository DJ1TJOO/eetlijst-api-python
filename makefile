.PHONY: format lint type

format:
	python -m isort src
	python -m black src

lint:
	python -m pylint src

type:
	python -m mypy src
