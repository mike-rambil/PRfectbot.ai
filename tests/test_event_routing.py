import pytest
from fastapi.testclient import TestClient
from prfectbot.main import app

client = TestClient(app)

PR_COMMENT_EVENT = {
    'action': 'created',
    'issue': {'number': 42},
    'repository': {
        'owner': {'login': 'octocat'},
        'name': 'Hello-World',
    },
    'comment': {'body': '@PRfectbot fix this please'},
}

PUSH_EVENT = {
    'ref': 'refs/heads/main',
    'before': 'oldsha',
    'after': 'newsha',
    'repository': {
        'owner': {'login': 'octocat'},
        'name': 'Hello-World',
    },
}


def test_webhook_accepts_pr_comment_event():
    headers = {"X-GitHub-Event": "issue_comment"}
    response = client.post("/webhook", json=PR_COMMENT_EVENT, headers=headers)
    assert response.status_code == 200
    # You can later check for more specific response content


def test_webhook_ignores_push_event():
    headers = {"X-GitHub-Event": "push"}
    response = client.post("/webhook", json=PUSH_EVENT, headers=headers)
    assert response.status_code == 204  # No Content, ignored 