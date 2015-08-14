import pytest
from leafman.api import suggest, jaccard


def test_suggest():
    suggested = suggest('abc', ['abc', 'abcdef'])
    expected = [('abc', 1.0), ('abcdef', 0.5)]
    assert list(suggested) == expected


def test_jaccard():
    u = jaccard('a')
    assert u('') == 0.0
    assert u('b') == 0.0
    assert u('a') == 1.0
    assert u('ab') == 0.5
    assert u('abcd') == 0.25
