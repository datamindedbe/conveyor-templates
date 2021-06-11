FROM python:3.8-slim

WORKDIR /app

{%- if cookiecutter.python_package_management == "pipenv" %}
RUN pip install pipenv
COPY . .
RUN PIP_NO_CACHE_DIR=true pipenv install --system
{%- endif %}
{%- if cookiecutter.python_package_management == "pip-tools" %}
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
RUN pip install -e .
{%- endif %}

