import pytest
from fastapi.testclient import TestClient
from prfectbot.main import app
from unittest.mock import patch

client = TestClient(app)

PR_COMMENT_FIX_EVENT = {
    "action": "created",
    "pull_request": {
        "number": 101,
        "head": {
            "ref": "feature-branch",
            "repo": {
                "owner": {"login": "octocat"},
                "name": "Hello-World",
            },
        },
    },
    "repository": {
        "owner": {"login": "octocat"},
        "name": "Hello-World",
    },
    "issue": {"number": 101},
    "comment": {"body": "@PRfectbot fix this please"},
}

PR_COMMENT_NO_FIX_EVENT = {
    "action": "created",
    "issue": {"number": 42},
    "repository": {
        "owner": {"login": "octocat"},
        "name": "Hello-World",
    },
    "comment": {"body": "@PRfectbot just checking in"},
}

PUSH_EVENT = {
    "ref": "refs/heads/main",
    "before": "oldsha",
    "after": "newsha",
    "repository": {
        "owner": {"login": "octocat"},
        "name": "Hello-World",
    },
}


def test_webhook_accepts_pr_comment_event_with_fix():
    headers = {"X-GitHub-Event": "issue_comment"}
    response = client.post("/webhook", json=PR_COMMENT_FIX_EVENT, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "fix requested"}


def test_webhook_accepts_pr_comment_event_without_fix():
    headers = {"X-GitHub-Event": "issue_comment"}
    response = client.post("/webhook", json=PR_COMMENT_NO_FIX_EVENT, headers=headers)
    assert response.status_code == 204


def test_webhook_ignores_push_event():
    headers = {"X-GitHub-Event": "push"}
    response = client.post("/webhook", json=PUSH_EVENT, headers=headers)
    assert response.status_code == 204  # No Content, ignored


def test_webhook_calls_clone_pr_branch_on_fix():
    headers = {"X-GitHub-Event": "issue_comment"}
    with patch("prfectbot.main.clone_pr_branch") as mock_clone:
        mock_clone.return_value = True
        response = client.post("/webhook", json=PR_COMMENT_FIX_EVENT, headers=headers)
        # Should be called with correct arguments (repo_owner, repo_name, branch, tmpdir)
        assert mock_clone.call_count == 1
        assert response.status_code == 200
