def test_python_template(cookies):
    result = cookies.bake(template="project/python", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
