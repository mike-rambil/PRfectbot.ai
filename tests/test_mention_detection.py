import pytest
from prfectbot.github_events import is_fix_requested


def test_detects_mention_and_fix():
    assert is_fix_requested("@PRfectbot fix this please")
    assert is_fix_requested("Hey @PRfectbot, can you fix errors?")
    assert is_fix_requested("@PRfectbot fix the PEP8 issues here")


def test_detects_mention_without_fix():
    assert not is_fix_requested("@PRfectbot just checking in")
    assert not is_fix_requested("@PRfectbot, what do you think?")


def test_no_mention():
    assert not is_fix_requested("Please fix this")
    assert not is_fix_requested("Hey bot, fix this") 