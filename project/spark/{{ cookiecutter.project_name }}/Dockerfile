{% if cookiecutter.spark_version == "2.4" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:2.4.3-{{ cookiecutter.scala_version }}-hadoop-2.9.2-v3
{%- elif cookiecutter.spark_version == "3.0" -%}
FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.1-hadoop-3.3.0
{%- endif %}

COPY build/libs/*-all.jar /opt/spark/work-dir/app.jar
