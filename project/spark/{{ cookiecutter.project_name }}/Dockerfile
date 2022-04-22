{% if cookiecutter.spark_version == "2.4" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:2.4.3-2.11-hadoop-2.9.2-v3
{%- elif cookiecutter.spark_version == "3.0" -%}


{% if cookiecutter.cloud == "aws" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.2.1-2.13-hadoop-3.3.1-v3
{%- elif cookiecutter.cloud == "azure" -%}
FROM public.ecr.aws/dataminded/spark-k8s-azure:3.2.1-2.13-hadoop-3.3.1-v1
{%- endif %}

{%- endif %}

COPY build/libs/*-all.jar /opt/spark/work-dir/app.jar
