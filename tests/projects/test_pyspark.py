import os
import subprocess


def assert_template_succeeds(result):
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project_path.is_dir()


def assert_first_line(file, content):
    with open(file) as f:
        first_line = f.readline().rstrip()
        assert content in first_line


def test_pyspark_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={},
    )
    assert_template_succeeds(result)
    assert_first_line(
        result.project_path / "Dockerfile",
        "FROM public.ecr.aws/dataminded/spark-k8s-glue",
    )


def test_pyspark_template_azure(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"cloud": "azure", "conveyor_managed_role": True},
    )
    assert_template_succeeds(result)
    assert not (result.project_path / "resources").is_dir()
    assert_batch_files(result)


def test_pyspark_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"conveyor_managed_role": False},
    )
    assert_template_succeeds(result)
    assert not (result.project_path / "resources").is_dir()


def assert_project_can_be_build(result):
    assert_template_succeeds(result)
    process = subprocess.Popen(
        ["docker", "build", "."],
        cwd=result.project_path,
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


def test_pyspark_template_spark(cookies):
    """
    This test makes sure that when a project with spark 3 support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
    )
    assert_project_can_be_build(result)


def test_pyspark_template_spark_pipenv(cookies):
    """
    This test makes sure that when a project with pipenv support is being rendered the docker image can be build
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/pyspark",
        extra_context={"python_package_management": "pipenv"},
    )
    assert_project_can_be_build(result)


def assert_streaming_files(result, exist: bool = True):
    assert (result.project_path / "streaming.yaml").is_file() == exist
    assert (result.project_path / "src/pyspark/streaming_app.py").is_file() == exist


def assert_batch_files(result, exist: bool = True):
    assert (result.project_path / "dags").is_dir() == exist
    assert (result.project_path / "src/pyspark/transformations").is_dir() == exist
    assert (result.project_path / "src/pyspark/app.py").is_file() == exist


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
