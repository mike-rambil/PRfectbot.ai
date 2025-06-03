import sys
import os
from unittest.mock import MagicMock
import prfectbot.gitutils
from prfectbot.gitutils import detect_code_changes_v2

print("sys.path:", sys.path)
print("cwd:", os.getcwd())
print("prfectbot.gitutils path:", prfectbot.gitutils.__file__)


# Example function to detect code changes (to be implemented in main code)
def detect_code_changes(repo_dir):
    pass


def test_no_code_changes():
    mock_result = MagicMock()
    mock_result.stdout = ""
    mock_result.returncode = 0

    def mock_run(*args, **kwargs):
        return mock_result

    assert detect_code_changes_v2("/tmp/clone", run=mock_run) == []


def test_some_code_changes():
    mock_result = MagicMock()
    mock_result.stdout = "M file1.py\nA file2.py\n"
    mock_result.returncode = 0

    def mock_run(*args, **kwargs):
        return mock_result

    assert detect_code_changes_v2("/tmp/clone", run=mock_run) == [
        "M file1.py",
        "A file2.py",
    ]


def test_detect_code_changes_error():
    def mock_run(*args, **kwargs):
        raise Exception("fail")

    assert detect_code_changes_v2("/tmp/clone", run=mock_run) is None
