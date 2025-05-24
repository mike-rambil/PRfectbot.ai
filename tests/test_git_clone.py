import pytest
from unittest.mock import patch
from prfectbot.gitutils import clone_pr_branch, run_git_clone


def test_clone_pr_branch_success():
    with patch('prfectbot.gitutils.run_git_clone') as mock_clone:
        mock_clone.return_value = True
        result = clone_pr_branch('octocat', 'Hello-World', 'feature-branch', '/tmp/clone')
        mock_clone.assert_called_once_with('https://github.com/octocat/Hello-World.git', 'feature-branch', '/tmp/clone')
        assert result is True


def test_clone_pr_branch_invalid_input():
    with patch('prfectbot.gitutils.run_git_clone') as mock_clone:
        result = clone_pr_branch('', '', '', '/tmp/clone')
        mock_clone.assert_not_called()
        assert result is False


def test_run_git_clone_success():
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = None
        assert run_git_clone('https://github.com/octocat/Hello-World.git', 'main', '/tmp/clone') is True
        mock_run.assert_called_once()


def test_run_git_clone_failure():
    with patch('subprocess.run', side_effect=Exception("fail")) as mock_run:
        assert run_git_clone('https://github.com/octocat/Hello-World.git', 'main', '/tmp/clone') is False
        mock_run.assert_called_once() 