{% if cookiecutter.spark_version == "2.4" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:2.4.3-2.11-hadoop-2.9.2-v3
RUN rm -rf /usr/bin/pip && ln -s /usr/bin/pip3.6 /usr/bin/pip && ln -s /usr/bin/pip3.6 /usr/bin/pip3
{%- elif cookiecutter.spark_version == "3.0" -%}

{% if cookiecutter.cloud == "aws" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.2.0-2.13-hadoop-3.3.1-v3
{%- elif cookiecutter.cloud == "azure" -%}
FROM public.ecr.aws/dataminded/spark-k8s-azure:3.2.0-hadoop-3.3.1-v1
{%- endif %}

{%- endif %}

ENV PYSPARK_PYTHON python3
WORKDIR /opt/spark/work-dir
{% if cookiecutter.spark_version == "3.0" -%}
USER 0
{%- endif %}

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
RUN pip3 install .
{% if cookiecutter.spark_version == "3.0" -%}
ARG spark_uid=185
USER ${spark_uid}
{%- endif %}