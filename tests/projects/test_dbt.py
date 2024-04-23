import json
import os

from project.dbt.hooks.post_gen_project import initialize_dbt_in_dir


def assert_file_contains_content(file, content):
    file_content = open(file).read()
    assert content in file_content


def test_dbt_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.is_dir()


def test_dbt_duckdb_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={"database_type": "duckdb", "project_name": "duckdb_test"},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert_file_contains_content(
        result.project_path / "dags/duckdb_test.py", "ConveyorContainerOperatorV2("
    )
    assert result.project_path.joinpath("query_duckdb.python").exists()


def test_dbt_duckdb_not_conveyor_managed_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={
            "database_type": "duckdb",
            "project_name": "duckdb_test",
            "conveyor_managed_role": "No",
        },
    )
    assert 0 == result.exit_code
    assert result.exception is None
    with open(result.project_path / "dags/duckdb_test.py") as file:
        file_content = file.read()
    assert "aws_role" not in file_content


def test_dbt_duckdb_conveyor_managed_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={
            "database_type": "duckdb",
            "project_name": "duckdb_test",
            "conveyor_managed_role": "Yes",
        },
    )
    assert 0 == result.exit_code
    assert result.exception is None
    with open(result.project_path / "dags/duckdb_test.py") as file:
        file_content = file.read()
    assert "aws_role" in file_content


def test_dbt_postgres_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={"database_type": "postgres", "project_name": "postgres_test"},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert_file_contains_content(
        result.project_path / "dags/postgres_test.py", "factory.add_tasks_to_dag("
    )
    assert not result.project_path.joinpath("query_duckdb.python").exists()


def test_dbt_template_azure(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={"cloud": "azure"},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.is_dir()
    assert not result.project_path.joinpath("/resources").is_dir()


def test_dbt_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={"conveyor_managed_role": False},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.is_dir()
    assert not result.project_path.joinpath("/resources").is_dir()


def test_db_init_all_db_types(tmpdir):
    with open(
        f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt/cookiecutter.json"
    ) as json_file:
        data = json.load(json_file)
        for db_type in data["database_type"]:
            tmpdir.mkdir(db_type)
            initialize_dbt_in_dir(os.path.join(tmpdir.strpath, db_type))
