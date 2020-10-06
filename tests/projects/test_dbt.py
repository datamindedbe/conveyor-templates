def test_dbt_template(cookies):
    result = cookies.bake(template="project/dbt", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()


def test_dbt_template_no_role(cookies):
    result = cookies.bake(
        template="project/dbt", extra_context={"role_creation": "none"}
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()
