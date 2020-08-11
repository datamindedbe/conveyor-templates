{% if cookiecutter.spark_version == "2.4" -%}
FROM datamindedbe/spark-k8s-glue:2.4.3-2.12-hadoop-2.9.2-v2
{%- elif cookiecutter.spark_version == "3.0" -%}
FROM datamindedbe/spark-k8s-glue:3.0.0-hadoop-3.2.1
{%- endif %}

ENV PYSPARK_PYTHON python3
WORKDIR /opt/spark/work-dir
{% if cookiecutter.spark_version == "3.0" -%}
USER 0
{%- endif %}

{%- if cookiecutter.python_package_management == "pipenv" %}
COPY . .
RUN pip3 install pipenv
RUN PIP_NO_CACHE_DIR=true pipenv install --system
{%- endif %}
{%- if cookiecutter.python_package_management == "pip-tools" %}
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
RUN pip3 install -e .
{%- endif %}
{% if cookiecutter.spark_version == "3.0" -%}
ARG spark_uid=185
USER ${spark_uid}
{%- endif %}