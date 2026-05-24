"""Acceptance tests for TASK 03 — parse_tags helper."""
from app import parse_tags


def test_basic_two_tags():
    assert parse_tags("work, urgent") == ["work", "urgent"]


def test_extra_whitespace_and_empty_slots():
    assert parse_tags(" school , , personal ") == ["school", "personal"]


def test_empty_string_returns_empty_list():
    assert parse_tags("") == []
