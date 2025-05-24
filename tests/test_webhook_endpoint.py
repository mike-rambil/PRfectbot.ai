import pytest
from fastapi.testclient import TestClient
from prfectbot.main import app

client = TestClient(app)


def test_webhook_post():
    headers = {"X-GitHub-Event": "issue_comment"}
    data = {"comment": {"body": "@PRfectbot fix this please"}}
    response = client.post("/webhook", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "fix requested"}
