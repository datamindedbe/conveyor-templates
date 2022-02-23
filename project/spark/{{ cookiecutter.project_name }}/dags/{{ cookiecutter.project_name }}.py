from airflow import DAG
from datafy.operators import DatafySparkSubmitOperatorV2
from airflow.utils import dates
from datetime import timedelta

default_args = {
    "owner": "Datafy",
    "depends_on_past": False,
    "start_date": dates.days_ago(2),
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


dag = DAG(
    "{{ cookiecutter.project_name }}",
    default_args=default_args,
    schedule_interval="@daily",
    max_active_runs=1,
)

sample_task = DatafySparkSubmitOperatorV2(
    dag=dag,
    task_id="sample",
    num_executors="1",
    driver_instance_type="mx.small",
    executor_instance_type="mx.small",
    {% if cookiecutter.spark_version == "2.4" -%}
    spark_main_version=2,
    {%- elif cookiecutter.spark_version == "3.0" -%}
    spark_main_version=3,
    {%- endif %}
    aws_role="{{ cookiecutter.project_name }}-{% raw %}{{ macros.datafy.env() }}{% endraw %}",
    {% if cookiecutter.spark_version == "2.4" -%}
    application="/opt/spark/work-dir/app.jar",
    {%- elif cookiecutter.spark_version == "3.0" -%}
    application="local:///opt/spark/work-dir/app.jar",
    {%- endif %}
    java_class="{{ cookiecutter.group_id }}.{{ cookiecutter.module_name }}.SampleJob",
    application_args=[{% raw %}"--date", "{{ ds }}", "--environment", "{{ macros.datafy.env() }}"{% endraw %}],
)
