import os
import subprocess


def assert_template_succeeds(result):
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()


def assert_first_line(file, content):
    with open(file) as f:
        firstline = f.readline().rstrip()
        assert firstline.__contains__(content)


def test_pyspark_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={},
    )
    assert_template_succeeds(result)
    assert_first_line(
        result.project + "/Dockerfile",
        "FROM public.ecr.aws/dataminded/spark-k8s-glue",
    )


def test_pyspark_template_azure(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"cloud": "azure", "conveyor_managed_role": True},
    )
    assert_template_succeeds(result)
    assert not (result.project + "/resources").isdir()
    assert_batch_files(result)


def test_pyspark_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"conveyor_managed_role": False},
    )
    assert_template_succeeds(result)
    assert not (result.project + "/resources").isdir()


def assert_project_can_be_build(result):
    assert_template_succeeds(result)
    process = subprocess.Popen(
        ["docker", "build", "."],
        cwd=result.project,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (
        stdout,
        stderr,
    ) = (
        process.communicate()
    )  # You can use stdout and stderr to find out what went wrong
    return_code = process.poll()
    assert return_code == 0, stdout + stderr


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
        extra_context={"spark_version": "2.4"},
    )
    assert_project_can_be_build(result)


def test_pyspark_template_spark_pipenv_2_4(cookies):
    """
    This test makes sure that when a project with pipenv support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"python_package_management": "pipenv", "spark_version": "2.4"},
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


def test_pyspark_template_streaming_spark_2(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"project_type": "streaming", "spark_version": "2.4"},
    )
    assert -1 == result.exit_code, result.exception
    assert result.exception is not None


def assert_streaming_files(result, exist: bool = True):
    assert (result.project + "/streaming.yaml").isfile() == exist
    assert (result.project + "/src/pyspark/streaming_app.py").isfile() == exist


def assert_batch_files(result, exist: bool = True):
    assert (result.project + "/dags").isdir() == exist
    assert (result.project + "/src/pyspark/transformations").isdir() == exist
    assert (result.project + "/src/pyspark/app.py").isfile() == exist


def test_pyspark_template_only_batch(cookies):
    """
    This tests checks that if streaming is disabled the streaming resources are cleaned up
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"project_type": "batch"},
    )
    assert_template_succeeds(result)
    assert_streaming_files(result, exist=False)
    assert_batch_files(result, exist=True)


def test_pyspark_template_only_streaming(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"project_type": "streaming"},
    )
    assert_template_succeeds(result)
    assert_streaming_files(result, exist=True)
    assert_batch_files(result, exist=False)


def test_pyspark_template_batch_and_streaming(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"project_type": "batch-and-streaming"},
    )
    assert_template_succeeds(result)
    assert_streaming_files(result, exist=True)
    assert_batch_files(result, exist=True)
