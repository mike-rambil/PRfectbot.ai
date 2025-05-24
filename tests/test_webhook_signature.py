import pytest
import hmac
import hashlib

# Example function to verify signature (to be implemented in main code)
def verify_github_signature(secret, payload, signature):
    mac = hmac.new(secret.encode(), msg=payload, digestmod=hashlib.sha256)
    expected = 'sha256=' + mac.hexdigest()
    return hmac.compare_digest(expected, signature)


def test_valid_signature():
    secret = 'testsecret'
    payload = b'{"action": "opened"}'
    mac = hmac.new(secret.encode(), msg=payload, digestmod=hashlib.sha256)
    signature = 'sha256=' + mac.hexdigest()
    assert verify_github_signature(secret, payload, signature)


def test_invalid_signature():
    secret = 'testsecret'
    payload = b'{"action": "opened"}'
    signature = 'sha256=invalidsignature'
    assert not verify_github_signature(secret, payload, signature) 