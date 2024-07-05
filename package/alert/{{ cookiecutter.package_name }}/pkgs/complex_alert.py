from conveyor import packages
from conveyor.operators import ConveyorContainerOperatorV2


def complex_failure_alert(ctx) -> None:
    """
    Trigger a ConveyorContainer operator containing the alerting code when a pipeline fails.
    :param ctx: Airflow context
    :return: None
    """
    ti = ctx["task_instance"]
    execution_date = ti.execution_date.isoformat()
    start_date = ti.start_date.isoformat()

    arguments = [
        "--state",
        str(ti.state),
        "--task",
        ti.task_id,
        "--dag",
        ti.dag_id,
        "--env",
        ctx["macros"].conveyor.env(),
        "--execution-date",
        execution_date,
        "--start-date",
        start_date,
        "--try-number",
        str(ti.try_number - 1),
    ]

    operator = ConveyorContainerOperatorV2(
        task_id="failure-container-alert-callback",
        image=packages.image(),
        validate_docker_image_exists=False,
        instance_type="mx_nano",
        arguments=arguments,
    )

    # Rendering the template fields is necessary even if we do not use templated values
    # because it renders some default arguments set by Conveyor (such as the environment).
    operator.render_template_fields(ctx, jinja_env=ctx["dag"].get_template_env())
    operator.execute(context=ctx)
