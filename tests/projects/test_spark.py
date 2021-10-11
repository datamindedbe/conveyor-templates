import os
import subprocess


def test_spark_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()


def test_spark_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"datafy_managed_role": False},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()


def test_spark_streaming_2_4(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"project_type": "streaming", "spark_version": "2.4"},
    )
    assert -1 == result.exit_code, result.exception
    assert result.exception is not None


def test_spark_spark_3_0_scala_2_11(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"scala_version": "2.11", "spark_version": "3.0"},
    )
    assert -1 == result.exit_code, result.exception
    assert result.exception is not None


def test_spark_project_type_batch(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"project_type": "batch"},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert_batch_files(result, exist=True)
    assert_streaming_files(result, exist=False)


def test_spark_project_type_streaming(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"project_type": "streaming"},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert_batch_files(result, exist=False)
    assert_streaming_files(result, exist=True)


def test_spark_project_type_batch_and_streaming(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"project_type": "batch-and-streaming"},
    )
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    assert_batch_files(result, exist=True)
    assert_streaming_files(result, exist=True)


def assert_streaming_files(result, exist: bool = True):
    assert (result.project + "/streaming.yaml").isfile() == exist
    assert (
        result.project + "/src/main/scala/cloud/datafy/spark/StreamingApp.scala"
    ).isfile() == exist


def assert_batch_files(result, exist: bool = True):
    assert (result.project + "/dags").isdir() == exist
    assert (
        result.project + "/src/main/scala/cloud/datafy/spark/SampleJob.scala"
    ).isfile() == exist
    assert (
        result.project + "/src/main/scala/cloud/datafy/spark/transformations"
    ).isdir() == exist


def assert_tests_run_without_compilation_issues(result):
    assert 0 == result.exit_code, result.exception
    assert result.exception is None
    process = subprocess.Popen(
        ["./gradlew", "test"],
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


def test_spark_template_spark_3(cookies):
    """
    This test makes sure that when a project with spark 3 support is being rendered the tests can be run
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"spark_version": "3.0"},
    )
    assert_tests_run_without_compilation_issues(result)


def test_spark_template_spark_2(cookies):
    """
    This test makes sure that when a project with spark 3 support is being rendered the tests can be run
    """
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/spark",
        extra_context={"spark_version": "2.0"},
    )
    assert_tests_run_without_compilation_issues(result)
