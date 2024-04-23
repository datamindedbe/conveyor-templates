test: flake8 black
	. venv/bin/activate; pytest tests

flake8:
	. venv/bin/activate; flake8 tests

black:
	. venv/bin/activate; black tests

requirements:
	pip-compile requirements.in --upgrade
	pip-compile dev-requirements.in --upgrade

install:
	python3 -m venv venv
	. venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install -r dev-requirements.txt
