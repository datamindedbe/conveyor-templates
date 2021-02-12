# {{ cookiecutter.project_name|capitalize}}

## Prerequisites

- [dbt](https://docs.getdbt.com/dbt-cli/installation/)
- [pyenv](https://github.com/pyenv/pyenv) (recommended)


## Project Structure

```bash
root/
 |-- dags/
 |   |-- project.py
 |-- dbt/
 |   |-- project/
 |   Dockerfile
```

## Concepts

### Pin your python dependencies
In building your Python application and its dependencies for production, you want to make sure that your builds are predictable and deterministic.
 Therefore, always pin your dependencies. You can read more in the article: [Better package management](https://nvie.com/posts/better-package-management/)

### dbt project structure
Consult the following documentation regarding [best practices for project structure](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355)

## Commands
Setup virtual environment:
- `pyenv local 3.6.x` to use a correct python version
- `python -m venv venv` to create a virtual environment
- `source ./venv/bin/activate` to activate the virtual environment
- `pip install pip-tools` to install pip tools

Tasks:
- `pip-compile requirements.in` to regenerate the requirements.txt

For some of the most used Dbt commands a makefile has been added to the project that passes the correct flags to dbt:
- `make run` executes dbt run
- `make test` executes dbt test
- `make debug` executes dbt debug, is useful to debug your connection to the database
- `make docs` executes dbt docs

Consult the [dbt documentation](https://docs.getdbt.com/docs/introduction) for additional commands.