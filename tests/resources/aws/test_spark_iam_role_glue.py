from os import path


def test_test_spark_iam_role_glue_template(cookies):
    result = cookies.bake(template="resource/aws/spark-iam-role-glue", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert path.isdir(result.project.dirname)
    assert path.isdir(path.join(result.project.dirname, "resources"))
