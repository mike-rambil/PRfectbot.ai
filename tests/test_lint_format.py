from unittest.mock import patch
from prfectbot.gitutils import run_linter_formatter


def test_run_linter_formatter_success():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = None
        assert run_linter_formatter("black", "/tmp/clone") is True
        mock_run.assert_called_once_with(["black", "/tmp/clone"], check=True)


def test_run_linter_formatter_failure():
    with patch("subprocess.run", side_effect=Exception("fail")) as mock_run:
        assert run_linter_formatter("black", "/tmp/clone") is False
        mock_run.assert_called_once_with(["black", "/tmp/clone"], check=True)
