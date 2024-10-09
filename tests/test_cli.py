from click.testing import CliRunner
from cloudmesh.cli import hello

def test_hello_command():
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert "Hello from CloudMesh!" in result.output
