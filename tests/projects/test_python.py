import os


def test_python_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/python",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/Pipfile").exists()
    assert not (result.project + "/Pipfile.lock").exists()
    assert (result.project + "/requirements.in").exists()
    assert (result.project + "/requirements.txt").exists()
    assert (result.project + "/dev-requirements.in").exists()
    assert (result.project + "/dev-requirements.txt").exists()


def test_python_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/python",
        extra_context={"conveyor_managed_role": False},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()


def test_python_template_azure(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/python",
        extra_context={"cloud": "azure"},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()
