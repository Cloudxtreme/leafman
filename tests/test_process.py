from pytest import fixture
from leafman.strategy import relevance
from leafman.process import suggest, extract, relative_best


@fixture
def res():
    return list(suggest('q', ['q1', 'q123'], threshold=0.25))


def test_suggest(res):
    assert res == [('q1', 0.5), ('q123', 0.25)]


def test_suggest_threshold():
    s = suggest('q', ['1234', '5678'], threshold=0.0)
    assert len(list(s)) == 2


def test_suggest_strategy():
    s = suggest('dna', ['dnaqb', 'dan'], strategy=relevance)
    assert len(list(s)) == 1


def test_extract(res):
    assert extract(res) == [('q1', 0.5), ('q123', 0.25)]
    assert extract(res, limit=1) == [('q1', 0.5)]
    assert extract(res, limit=0) == []


def test_relative_best(res):
    s = relative_best(res)
    assert extract(s) == [('q1', 0.5)]
