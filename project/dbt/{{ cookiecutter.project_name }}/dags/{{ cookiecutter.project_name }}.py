from airflow import DAG
from airflow.operators.datafy_container_plugin import DatafyContainerOperator
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


image = "{% raw %}{{ macros.image('{% endraw %}{{ cookiecutter.project_name }}{% raw %}') }}{% endraw %}"

dag = DAG(
    "{{ cookiecutter.project_name }}", default_args=default_args, schedule_interval="{{ cookiecutter.workflow_schedule }}", max_active_runs=1
)

DatafyContainerOperator(
    dag=dag,
    task_id="sample",
    name="sample",
    image=image,
    cmds=["dbt"],
    arguments=[
        "run",
        "--target",
        "{% raw %}{{ macros.env() }}{% endraw %}",
        "--profiles-dir",
        "./.."
    ],
    instance_type="mx_micro",
{%- if cookiecutter.role_creation != "none" %}
    service_account_name="{{ cookiecutter.project_name }}"
{%- endif %}
)
