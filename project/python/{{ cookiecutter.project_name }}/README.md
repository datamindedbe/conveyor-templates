# {{ cookiecutter.project_name|capitalize}}

## Prerequisites

{%- if cookiecutter.python_package_management == "pipenv" %}
- [pipenv](https://pipenv.kennethreitz.org/en/latest/)
{%- endif %}
- [pyenv](https://github.com/pyenv/pyenv) (recommended)

## Project Structure

```bash
root/
 |-- dags/
 |   |-- project.py
 |-- src/
 |   |-- project/
 |   |-- |-- common/
 |   |-- |-- |-- spark.py
 |   |-- |-- jobs/
 |   |-- |-- transformations/
 |   |-- app.py
 |-- tests/
 |   |-- common/
 |   |-- | -- spark.py
 |   Dockerfile
 |   setup.py
```

The main Python module contains the ETL job `app.py`. By default `app.py` accepts a number of arguments:
- `--date` the execution date
- `--env` the environment we are executing in
- `--jobs` one or more jobs that needs to be executed

## Concepts

### Pin your python dependencies
In building your Python application and its dependencies for production, you want to make sure that your builds are predictable and deterministic.
 Therefore, always pin your dependencies. You can read more in the article: [Better package management](https://nvie.com/posts/better-package-management/)

### Separate job breakdown from scheduling
Jobs can be found in the `jobs/` directory. A job function needs to be annotated with `@entrypoint("name")` and
the module needs to be imported in `app.py`. This approach is based on the article [Scaling a Mature Data Pipeline](https://medium.com/airbnb-engineering/scaling-a-mature-data-pipeline-managing-overhead-f34835cbc866)
 and can be used to manage scheduling overhead.

## Commands
{%- if cookiecutter.python_package_management == "pipenv" %}
If you are running the datafy cli in a virtual environment, make sure to set PIPENV_IGNORE_VIRTUALENVS=1. You can
also prefix every pipenv command e.g. `PIPENV_IGNORE_VIRTUALENVS=1 pipenv install --dev`

- `pipenv install --dev` to install the module and all dependencies in the virtual environment
- `pipenv run python -m pytest --cov=src tests` runs all the tests and check coverage
- `pipenv run black dags src tests --check` checks PEP8 compliance issues
- `pipenv run black dags src tests` fixes PEP8 compliance issues
- `pipenv check` Checks for security vulnerabilities and against PEP 508 markers
{%- endif %}
{%- if cookiecutter.python_package_management == "pip-tools" %}
Setup virtual environment:
- `pyenv local 3.6.x` to use a correct python version
- `python -m venv venv` to create a virtual environment
- `source ./venv/bin/activate` to activate the virtual environment
- `pip install pip-tools` to install pip tools

Tasks:
- `pip install -r requirements.txt` to install dependencies
- `pip install -r dev-requirements.txt` to install development dependencies
- `pip install -e .` to install the project in editable mode
- `python -m pytest --cov=src tests` runs all the tests and check coverage
- `python -m black dags src tests --check` checks PEP8 compliance issues
- `python -m black dags src tests` fixes PEP8 compliance issues
{%- endif %}