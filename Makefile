test: flake8 black
	. venv/bin/activate; pytest tests

flake8:
	. venv/bin/activate; flake8 tests

black:
	. venv/bin/activate; black tests

requirements:
	uv pip compile requirements.in --upgrade -o requirements.txt
	uv pip compile dev-requirements.in --upgrade -c requirements.txt -o dev-requirements.txt

install:
	python3 -m venv venv
	. venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install -r dev-requirements.txt
