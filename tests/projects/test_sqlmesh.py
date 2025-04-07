import os


def test_sqlmesh_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/sqlmesh",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.is_dir()


def test_sqlmesh_template_no_role(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../project/sqlmesh",
        extra_context={"conveyor_managed_role": False},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.is_dir()
    assert not result.project_path.joinpath("/resources").is_dir()