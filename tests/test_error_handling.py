import pytest
from unittest.mock import patch

# Example function to handle webhook event (to be implemented in main code)
def handle_webhook_event(event_type, payload):
    pass

def test_unsupported_event():
    assert handle_webhook_event('unknown_event', {}) == {'error': 'unsupported event'}

def test_missing_permissions():
    with patch('prfectbot.github_api.check_permissions', return_value=False):
        assert handle_webhook_event('issue_comment', {'permissions': 'none'}) == {'error': 'missing permissions'}

def test_failed_fix():
    with patch('prfectbot.gitutils.run_linter_formatter', return_value=False):
        assert handle_webhook_event('issue_comment', {'simulate': 'fail_fix'}) == {'error': 'fix failed'} 