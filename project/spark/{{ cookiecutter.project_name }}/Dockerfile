{% if cookiecutter.spark_version == "2.4" -%}
FROM datamindedbe/spark-k8s-glue:2.4.3-{{ cookiecutter.scala_version }}-hadoop-2.9.2-v2
{%- elif cookiecutter.spark_version == "3.0" -%}
FROM datamindedbe/spark-k8s-glue:v3.0.1-hadoop-3.3.0
{%- endif %}

COPY build/libs/*-all.jar /opt/spark/work-dir/app.jar
