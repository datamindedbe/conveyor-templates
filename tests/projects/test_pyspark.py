import os
import subprocess


def test_pyspark_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()


def test_pyspark_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"datafy_managed_role": False},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()


def assert_project_can_be_build(result):
    assert 0 == result.exit_code
    process = subprocess.Popen(
        ["docker", "build", "."],
        cwd=result.project,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (
        stdout,
        stderr,
    ) = process.communicate()  # You can use stoud and sterr to find out what went wrong
    return_code = process.poll()
    assert return_code == 0, stderr


def test_pyspark_template_spark_3(cookies):
    """
    This test makes sure that when a project with spark 3 support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"spark_version": "3.0"},
    )
    assert_project_can_be_build(result)


def test_pyspark_template_spark_2_4(cookies):
    """
    This test makes sure that when a project with spark 2.4 support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={},
    )
    assert_project_can_be_build(result)


def test_pyspark_template_spark_pipenv_2_4(cookies):
    """
    This test makes sure that when a project with pipenv support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"python_package_management": "pipenv"},
    )
    assert_project_can_be_build(result)


def test_pyspark_template_spark_pipenv_3(cookies):
    """
    This test makes sure that when a project with pipenv support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"python_package_management": "pipenv", "spark_version": "3.0"},
    )
    assert_project_can_be_build(result)
