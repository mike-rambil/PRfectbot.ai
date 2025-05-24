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


def test_extract_repo_branch_from_pr_event():
    payload = {
        'action': 'opened',
        'pull_request': {
            'number': 101,
            'head': {
                'ref': 'feature-branch',
                'repo': {
                    'owner': {'login': 'octocat'},
                    'name': 'Hello-World',
                },
            },
        },
        'repository': {
            'owner': {'login': 'octocat'},
            'name': 'Hello-World',
        },
    }
    from prfectbot.github_events import extract_pr_repo_branch
    result = extract_pr_repo_branch(payload)
    assert result['pr_number'] == 101
    assert result['repo_owner'] == 'octocat'
    assert result['repo_name'] == 'Hello-World'
    assert result['branch'] == 'feature-branch'


def test_extract_repo_branch_missing_fields():
    payload = {
        'action': 'opened',
        'pull_request': {
            'number': 101,
            'head': {},
        },
        'repository': {},
    }
    from prfectbot.github_events import extract_pr_repo_branch
    result = extract_pr_repo_branch(payload)
    assert result['pr_number'] == 101
    assert result['repo_owner'] is None
    assert result['repo_name'] is None
    assert result['branch'] is None 