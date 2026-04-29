import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))
from agent_test import _sanitize_selector


def test_none_passthrough():
    assert _sanitize_selector(None) is None


def test_clean_selector_unchanged():
    assert _sanitize_selector("button") == "button"
    assert _sanitize_selector("div.class") == "div.class"


def test_contains_only_raises():
    with pytest.raises(ValueError, match=":contains"):
        _sanitize_selector("a:contains(Click me)")


def test_all_blocked_raises():
    with pytest.raises(ValueError):
        _sanitize_selector("a:contains(foo), button:contains(bar)")


def test_partial_contains_stripped():
    assert _sanitize_selector("button, a:contains(link)") == "button"


def test_multiple_clean_unchanged():
    assert _sanitize_selector("div, span, button") == "div, span, button"


def test_whitespace_stripped_from_parts():
    assert _sanitize_selector("  button , span ") == "button, span"


def test_mixed_strips_contains_parts():
    assert _sanitize_selector("div, a:contains(text), span") == "div, span"
