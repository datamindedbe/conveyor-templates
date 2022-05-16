import os


def test_test_spark_iam_role_glue_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../../resource/aws/spark-iam-role-glue",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.parent.is_dir()
    assert result.project_path.parent.joinpath("resources").is_dir()
