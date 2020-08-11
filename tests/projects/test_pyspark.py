def test_pyspark_template(cookies):
    result = cookies.bake(template="project/pyspark", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
