import json
import os

from project.dbt.hooks.post_gen_project import initialize_dbt_in_dir


def test_dbt_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()


def test_dbt_template_azure(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={"cloud": "azure"},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()


def test_dbt_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt",
        extra_context={"datafy_managed_role": False},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project.isdir()
    assert not (result.project + "/resources").isdir()


def test_db_init_all_db_types(tmpdir):
    with open(
        f"{os.path.dirname(os.path.abspath(__file__))}/../../project/dbt/cookiecutter.json"
    ) as json_file:
        data = json.load(json_file)
        for db_type in data["database_type"]:
            tmpdir.mkdir(db_type)
            initialize_dbt_in_dir(os.path.join(tmpdir.strpath, db_type), db_type)
