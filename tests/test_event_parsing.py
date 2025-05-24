import pytest
from prfectbot.github_events import parse_pr_comment_event


def test_parse_pr_comment_event():
    payload = {
        'action': 'created',
        'issue': {'number': 42},
        'repository': {
            'owner': {'login': 'octocat'},
            'name': 'Hello-World',
        },
        'comment': {'body': '@PRfectbot fix this please'},
    }
    result = parse_pr_comment_event(payload)
    assert result['pr_number'] == 42
    assert result['repo_owner'] == 'octocat'
    assert result['repo_name'] == 'Hello-World'
    assert result['comment_body'] == '@PRfectbot fix this please' 