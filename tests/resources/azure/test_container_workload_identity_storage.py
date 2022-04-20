import os
from os import path


def test_container_workload_identity_storage(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../../resource/azure/container-workload-identity-storage",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert path.isdir(result.project.dirname)
    assert path.isdir(path.join(result.project.dirname, "terraform_resources"))
