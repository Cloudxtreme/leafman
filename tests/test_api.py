import pytest
from leafman.api import suggest


def test_suggest():
    suggested = suggest('abc', ['abc', 'abcdef'])
    expected = [('abc', 1.0), ('abcdef', 0.5)]
    assert list(suggested) == expected
