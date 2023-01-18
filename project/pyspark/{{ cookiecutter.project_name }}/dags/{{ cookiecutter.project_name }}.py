from airflow import DAG
from conveyor.operators import ConveyorSparkSubmitOperatorV2
from datetime import timedelta
from airflow.utils import dates


default_args = {
    "owner": "Conveyor",
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

sample_task = ConveyorSparkSubmitOperatorV2(
    dag=dag,
    task_id="sample",
    num_executors="1",
    driver_instance_type="mx.small",
    executor_instance_type="mx.small",
    {%- if cookiecutter.conveyor_managed_role %}
    aws_role="{{ cookiecutter.project_name }}-{% raw %}{{ macros.conveyor.env() }}{% endraw %}",
    {%- endif %}
    spark_main_version=3,
    application="local:///opt/spark/work-dir/src/{{ cookiecutter.module_name }}/app.py",
    application_args=["{% raw %}--date", "{{ ds }}", "--env", "{{ macros.conveyor.env() }}{% endraw %}"],
)
