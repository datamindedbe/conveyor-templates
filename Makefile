test: flake8 black
	pytest tests

flake8:
	flake8 tests

black:
	black tests