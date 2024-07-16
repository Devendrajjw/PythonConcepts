#install typer, pyyaml


from typer.testing import CliRunner
from typer_yaml_reader import app


def test_typer_yaml_with_list():
    runner = CliRunner()
    test_args = ['./config.yml', '--env', 'rest']
    result = runner.invoke(app, test_args)
    assert result.exit_code == 0
    # Use result.stdout to access the command's output
    output = result.stdout.rstrip()
    expected_output = "{'url': 'https://example.com/', 'port': 3001}"
    assert expected_output in output

