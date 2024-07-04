from airflow.models import Variable
from airflow.providers.opsgenie.hooks.opsgenie import OpsgenieAlertHook
from airflow.providers.slack.operators.slack_webhook import SlackWebhookHook
from airflow.utils.context import Context
from conveyor.alerting import conveyor_executions_url


def simple_opsgenie_alert(ctx: Context) -> None:
    """
    Trigger an opsgenie alert when a pipeline fails
    :param ctx: Airflow context
    :return: None
    """
    environment = Variable.get("environment", "unknown")
    task = ctx.get("task_instance")
    schedule = ctx.get("ts")
    reason = ctx.get("reason", "")
    message = (
        f'Environment ({environment}) DAG ({task.dag_id}) failed on task "{task.task_id}" (schedule: {schedule})'
    )
    hook = OpsgenieAlertHook()
    hook.create_alert(
        {
            "alias": f"{task.dag_id}-{task.task_id}-{schedule}",
            "message": message,
            "description": f"Reason of failure: {reason}",
            "priority": "P3",
        }
    )


def simple_slack_alert(ctx: Context) -> None:
    """
    Trigger a slack alert with a nice message when a pipeline fails
    :param ctx: Airflow context
    :return: None
    """
    env: str = Variable.get("environment", "unknown")
    dag = ctx.get("dag_run").dag_id
    exec_date = ctx.get("execution_date")
    reason = ctx.get("reason", "")
    url = conveyor_executions_url(ctx)
    slack_msg = f"""
            :red_circle: DAG `{dag}` in environment `{env}` failed.
            *DAG*: {dag}
            *Environment*: {env}
            *Execution Time*: {exec_date}
            *Reason*: {reason}
            *Url*: https://app.conveyordata.com/environments/{env}/airflow/tree?dag_id={dag}
            *ConveyorURL*: {url}
        """

    SlackWebhookHook(
        http_conn_id="slack_webhook",
        message=slack_msg,
    ).execute()
