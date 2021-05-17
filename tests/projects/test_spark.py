import os


def test_spark_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()


def test_spark_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"datafy_managed_role": False},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()
