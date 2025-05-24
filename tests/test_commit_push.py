import pytest
from unittest.mock import patch
from prfectbot.gitutils import commit_and_push_fixes

def test_commit_and_push_success():
    with patch('prfectbot.gitutils.detect_code_changes_v2', return_value=['M file1.py']), \
         patch('subprocess.run') as mock_run:
        mock_run.return_value.returncode = 0
        assert commit_and_push_fixes('/tmp/clone', 'feature-branch') is True
        assert mock_run.call_count >= 2  # At least commit and push

def test_commit_and_push_no_changes():
    with patch('prfectbot.gitutils.detect_code_changes_v2', return_value=[]), \
         patch('subprocess.run') as mock_run:
        mock_run.return_value.returncode = 0
        assert commit_and_push_fixes('/tmp/clone', 'feature-branch') is False

def test_commit_and_push_error():
    with patch('prfectbot.gitutils.detect_code_changes_v2', return_value=['M file1.py']), \
         patch('subprocess.run', side_effect=Exception('fail')) as mock_run:
        assert commit_and_push_fixes('/tmp/clone', 'feature-branch') is False 