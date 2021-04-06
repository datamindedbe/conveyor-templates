from airflow import DAG
from datafy.operators import DatafySparkSubmitOperator
from datetime import datetime, timedelta


{% set start_date = cookiecutter.workflow_start_date.split('-') -%}
default_args = {
    "owner": "Datafy",
    "depends_on_past": False,
    "start_date": datetime(year={{ start_date[0] }}, month={{ start_date[1].lstrip("0") }}, day={{ start_date[2].lstrip("0") }}),
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


role = "{% raw %}eks-job-role-samples-{{ macros.datafy.env() }}{% endraw %}"

dag = DAG(
    "{{ cookiecutter.project_name }}", default_args=default_args, schedule_interval="{{ cookiecutter.workflow_schedule }}", max_active_runs=1
)

sample_task = DatafySparkSubmitOperator(
    dag=dag,
    task_id="sample",
    num_executors="1",
    driver_instance_type="mx_small",
    executor_instance_type="mx_small",
    env_vars={"AWS_REGION": "eu-west-1"},
    {% if cookiecutter.spark_version == "2.4" -%}
    spark_main_version=2,
    {%- elif cookiecutter.spark_version == "3.0" -%}
    spark_main_version=3,
    {%- endif %}
    conf={
        "spark.kubernetes.driver.annotation.iam.amazonaws.com/role": role,
        "spark.kubernetes.executor.annotation.iam.amazonaws.com/role": role,
    },
    {% if cookiecutter.spark_version == "2.4" -%}
    application="/opt/spark/work-dir/app.jar",
    {%- elif cookiecutter.spark_version == "3.0" -%}
    application="local:///opt/spark/work-dir/app.jar",
    {%- endif %}
    java_class="{{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.RouterApp",
    application_args=[{% raw %}"--date", "{{ ds }}", "--jobs", "sample", "--environment", "{{ macros.datafy.env() }}"{% endraw %}],
)
