{% if cookiecutter.spark_version == "2.4" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:2.4.3-2.11-hadoop-2.9.2-v3
RUN rm -rf /usr/bin/pip && ln -s /usr/bin/pip3.6 /usr/bin/pip && ln -s /usr/bin/pip3.6 /usr/bin/pip3
{%- elif cookiecutter.spark_version == "3.0" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.1-hadoop-3.3.0
{%- endif %}

ENV PYSPARK_PYTHON python3
WORKDIR /opt/spark/work-dir

{% if cookiecutter.spark_version == "3.0" -%}
USER 0
{%- endif %}

RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*
COPY src/requirements.txt src/requirements.txt
RUN pip3 install -r src/requirements.txt
RUN rm -rf /usr/bin/python && ln -s python3 /usr/bin/python && pip3 install --upgrade pip
COPY . .

{% if cookiecutter.spark_version == "3.0" -%}
ARG spark_uid=185
USER ${spark_uid}
{%- endif %}