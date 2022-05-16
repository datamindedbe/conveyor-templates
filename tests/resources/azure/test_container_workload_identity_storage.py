import os


def test_container_workload_identity_storage(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../../resource/azure/container-workload-identity"
        f"-storage",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.parent.is_dir()
    assert result.project_path.parent.joinpath("terraform_resources").is_dir()
