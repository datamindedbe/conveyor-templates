import os


def test_container_iam_role_s3(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../../resource/aws/container-iam-role-s3",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.parent.is_dir()
    assert result.project_path.parent.joinpath("resources").is_dir()
