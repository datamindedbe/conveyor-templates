from airflow import DAG
from datetime import datetime, timedelta

from conveyor import packages
from conveyor.operators import ConveyorContainerOperatorV2

simple_alert = packages.load("{{ cookiecutter.package_name }}.alert", trial=True)
complex_alert = packages.load("{{ cookiecutter.package_name }}.complex_alert", trial=True)

default_args = {
    "owner": "Data Minded",
    "depends_on_past": False,
    "start_date": datetime.now() - timedelta(days=2),
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "execution_timeout": timedelta(minutes=5),
}

with DAG(
        "example-dag-alert-complex-callback",
        default_args={
            **default_args,
            "on_failure_callback": complex_alert.complex_failure_alert,
        },
        schedule_interval="@daily",
        max_active_runs=1,
):
    ConveyorContainerOperatorV2(
        task_id="failing-task-with-complex-callback",
        cmds=["unexisting"],
        image="python:3.11.9-alpine",
    )

with DAG(
        "example-dag-alert-simple-callback",
        default_args={
            **default_args,
            "on_failure_callback": simple_alert.simple_slack_alert,
        },
        schedule_interval="@daily",
        max_active_runs=1,
):
    ConveyorContainerOperatorV2(
        task_id="failing-task-with-simple-callback",
        cmds=["unexisting"],
        image="python:3.11.9-alpine",
    )
