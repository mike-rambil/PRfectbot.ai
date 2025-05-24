import pytest
from unittest.mock import patch

# Example function to detect code changes (to be implemented in main code)
def detect_code_changes(repo_dir):
    pass

def test_no_code_changes():
    with patch('subprocess.run') as mock_run:
        mock_run.return_value.stdout = ''
        mock_run.return_value.returncode = 0
        assert detect_code_changes('/tmp/clone') == []
        mock_run.assert_called_once()

def test_some_code_changes():
    with patch('subprocess.run') as mock_run:
        mock_run.return_value.stdout = 'M file1.py\nA file2.py\n'
        mock_run.return_value.returncode = 0
        assert detect_code_changes('/tmp/clone') == ['M file1.py', 'A file2.py']
        mock_run.assert_called_once()

def test_detect_code_changes_error():
    with patch('subprocess.run', side_effect=Exception('fail')) as mock_run:
        assert detect_code_changes('/tmp/clone') is None
        mock_run.assert_called_once() 