import pytest
from click.testing import CliRunner
from cli_app import greet

def test_greet():
    runner = CliRunner()
    result = runner.invoke(greet, ['Alice'])
    assert result.exit_code == 0
    assert result.output.strip() == 'Hello, Alice!'

def test_greet_no_name():
    runner = CliRunner()
    result = runner.invoke(greet, [])
    assert result.exit_code != 0
    assert "Error: Missing argument 'NAME'" in result.output


