def test_python_template(cookies):
    result = cookies.bake(template="project/python", extra_context={})
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/Pipfile").exists()
    assert not (result.project + "/Pipfile.lock").exists()
    assert (result.project + "/requirements.in").exists()
    assert (result.project + "/requirements.txt").exists()
    assert (result.project + "/dev-requirements.in").exists()
    assert (result.project + "/dev-requirements.txt").exists()


def test_python_template_pipenv(cookies):
    result = cookies.bake(
        template="project/python",
        extra_context={"python_package_management": "pipenv"},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert (result.project + "/Pipfile").exists()
    assert (result.project + "/Pipfile.lock").exists()
    assert not (result.project + "/requirements.in").exists()
    assert not (result.project + "/requirements.txt").exists()
    assert not (result.project + "/dev-requirements.in").exists()
    assert not (result.project + "/dev-requirements.txt").exists()


def test_python_template_no_role(cookies):
    result = cookies.bake(
        template="project/python", extra_context={"role_creation": "none"}
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()
