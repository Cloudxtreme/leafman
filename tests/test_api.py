import pytest
from leafman.api import suggest, length_index


def test_suggest():
    suggested = suggest('abc', ['abc', 'abcdef'])
    expected = [('abc', 1.0), ('abcdef', 0.5)]
    assert list(suggested) == expected


def test_suggest_finder():
    s = suggest('abc', {'abc': ['abc']}, finder=dict)
    e = [('abc', 1.0)]
    assert list(s) == e


def test_length_index():
    u = length_index('a')
    assert u('') == 0.0
    assert u('1') == 1.0
    assert u('12') == 0.5
    assert u('1234') == 0.25
    assert u('1234567890') == 0.1
