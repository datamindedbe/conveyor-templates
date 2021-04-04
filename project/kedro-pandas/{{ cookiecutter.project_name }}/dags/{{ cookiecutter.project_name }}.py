from airflow import DAG
from datafy_airflow_plugins.datafy_container_plugin.datafy_container_operator import DatafyContainerOperator
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

dag = DAG(
    "{{ cookiecutter.project_name }}", default_args=default_args, schedule_interval="{{ cookiecutter.workflow_schedule }}", max_active_runs=1
)

DatafyContainerOperator(
    dag=dag,
    task_id="sample",
    name="sample",
    cmds=["kedro"],
    arguments=["run", "--env", "{% raw %}{{ macros.env() }}{% endraw %}"],
    instance_type="mx_micro",
)
