from airflow import DAG
from conveyor.factories import ConveyorDbtTaskFactory
from datetime import datetime, timedelta


{% set start_date = cookiecutter.workflow_start_date.split('-') -%}
default_args = {
    "owner": "Conveyor",
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

factory = ConveyorDbtTaskFactory(
{%- if cookiecutter.conveyor_managed_role %}
    task_aws_role="{{ cookiecutter.project_name }}-{% raw %}{{ macros.conveyor.env() }}{% endraw %}",
{%- endif %}
)
factory.add_tasks_to_dag(dag=dag)
