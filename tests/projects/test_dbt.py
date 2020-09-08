def test_dbt_template(cookies):
    result = cookies.bake(template="project/dbt", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
