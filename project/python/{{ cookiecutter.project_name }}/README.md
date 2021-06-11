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

The main Python module contains the ETL job `sample.py`. By default `sample.py` accepts a number of arguments:
- `--date` the execution date
- `--env` the environment we are executing in

## Concepts

### Pin your python dependencies
In building your Python application and its dependencies for production, you want to make sure that your builds are predictable and deterministic.
 Therefore, always pin your dependencies. You can read more in the article: [Better package management](https://nvie.com/posts/better-package-management/)

{%- if cookiecutter.python_package_management == "pip-tools" %}
When using pip-tools to manage dependencies, you define your dependencies in the `requirements.in` file.
This file can then be compiled into the `requirements.txt` file by running the command `pip-compile requirements.in` from your shell.

This compilation step makes sure every dependency gets pinned in the `requirements.txt` file,
ensuring that project won't break because of transitive dependencies being silently updated.
When a dependency does need to be updated, you can update the `requirements.in` file and re-compile it.
With this method, package updates always happen as a conscious decision by the developer.

The `pip-compile` command should be run from the same virtual environment as your project so conditional dependencies that require a specific Python version,
or other environment markers, resolve relative to your project's environment.
{%- endif %}

### Adding another job to the container

If you want to run another job in your container create a file like sample. You should:

- Use argparse (or something similar) to parse argument to pass to your job
- Have a main function that can be called
- Make sure you have `if __name__ == "__main__"` construct in your file like below
- Use your job file in a dag

The following python snippet makes sure that if you call this module from the command lind that the main() function will be
executed:

```python
if __name__ == "__main__":
    main()
```

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
- `pyenv local` to use a correct python version
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
- `pip-compile requirements.in` if you add new requirements this regenerates a new requirements.txt
- `pip-compile dev-requirements.in` if you add new requirements this regenerates a new dev-requirements.txt, you should also do this when have updated your requirements.in
{%- endif %}