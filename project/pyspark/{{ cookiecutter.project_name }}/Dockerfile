{% if cookiecutter.spark_version == "2.4" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:2.4.3-2.11-hadoop-2.9.2-v3
RUN rm -rf /usr/bin/pip && ln -s /usr/bin/pip3.6 /usr/bin/pip && ln -s /usr/bin/pip3.6 /usr/bin/pip3
{%- elif cookiecutter.spark_version == "3.0" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.0.1-hadoop-3.3.0
{%- endif %}

ENV PYSPARK_PYTHON python3
WORKDIR /opt/spark/work-dir
{% if cookiecutter.spark_version == "3.0" -%}
USER 0
{%- endif %}

{%- if cookiecutter.python_package_management == "pipenv" %}
RUN pip3 install pipenv
RUN rm -rf /usr/bin/python && ln -s python3 /usr/bin/python && pip3 install --upgrade pip
COPY . .
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