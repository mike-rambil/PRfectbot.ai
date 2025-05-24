import pytest
from fastapi.testclient import TestClient
from prfectbot.main import app

client = TestClient(app)

def test_webhook_post():
    headers = {"X-GitHub-Event": "issue_comment"}
    response = client.post("/webhook", json={"test": "data"}, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "received"} 