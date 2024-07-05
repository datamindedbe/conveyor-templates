.PHONY: build

build:

requirements:
	pip-compile requirements.in --no-header

install:
	python -m venv venv
	( \
       . venv/bin/activate; \
       pip install -r requirements.txt; \
       pip install -r dev-requirements.txt; \
       pip install -e .; \
    )

lint:
	. venv/bin/activate; \
	python3 -m black src; \
	python3 -m flake8 src; \
	python3 -m isort src; \
	python3 -m mypy src; \