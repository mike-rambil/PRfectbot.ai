import pytest
from unittest.mock import patch
from prfectbot.pr_processor import process_pull_request


def test_process_pull_request_flow():
    with patch('prfectbot.pr_processor.clone_pr_branch') as mock_clone, \
         patch('prfectbot.pr_processor.run_linter_formatter') as mock_lint, \
         patch('prfectbot.pr_processor.commit_and_push_fixes') as mock_commit, \
         patch('prfectbot.pr_processor.post_pr_comment') as mock_comment:
        mock_clone.return_value = True
        mock_lint.return_value = True
        mock_commit.return_value = True

        assert (
            process_pull_request('octocat', 'Hello-World', 'feature', 101) is True
        )
        mock_clone.assert_called_once()
        assert mock_lint.call_count == 2
        mock_commit.assert_called_once()
        mock_comment.assert_called_once_with(
            'octocat', 'Hello-World', 101, 'I have done linting and prettier checks.'
        )


def test_process_pull_request_missing_info():
    assert process_pull_request('', 'repo', 'branch', 1) is False
