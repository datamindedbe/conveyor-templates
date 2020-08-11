def test_spark_template(cookies):
    result = cookies.bake(template="project/spark", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
