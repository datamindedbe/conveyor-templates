import os


def test_spark_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
