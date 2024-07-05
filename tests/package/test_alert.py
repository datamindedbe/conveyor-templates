import os


def assert_file_contains_content(file, content):
    file_content = open(file).read()
    assert content in file_content


def test_alert_template(cookies):
    result = cookies.bake(
        template=f"{os.path.dirname(os.path.abspath(__file__))}/../../package/alert",
        extra_context={},
    )
    assert 0 == result.exit_code
    assert result.exception is None
    assert result.project_path.is_dir()
    assert_file_contains_content(result.project_path / "setup.py", 'name = "common"')
