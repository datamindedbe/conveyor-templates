from airflow import DAG
from datafy.operators import DatafySparkSubmitOperatorV2
from datetime import timedelta
from airflow.utils import dates


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
    driver_instance_type="mx_small",
    executor_instance_type="mx_small",
    aws_role="{{ cookiecutter.project_name }}-{% raw %}{{ macros.datafy.env() }}{% endraw %}",
    {% if cookiecutter.spark_version == "2.4" -%}
    spark_main_version=2,
    {%- elif cookiecutter.spark_version == "3.0" -%}
    spark_main_version=3,
    {%- endif %}
    {% if cookiecutter.spark_version == "2.4" -%}
    application="/opt/spark/work-dir/src/{{ cookiecutter.module_name }}/app.py",
    {%- elif cookiecutter.spark_version == "3.0" -%}
    application="local:///opt/spark/work-dir/src/{{ cookiecutter.module_name }}/app.py",
    {%- endif %}
    application_args=["{% raw %}--date", "{{ ds }}", "--env", "{{ macros.datafy.env() }}{% endraw %}"],
)
