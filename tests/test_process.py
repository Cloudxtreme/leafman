from leafman.strategy import relevance
from leafman.process import suggest, extract, best_of, relative_best


def test_suggest():
    s = suggest('q', ['q1', 'q2'])
    assert list(s) == [('q1', 0.5), ('q2', 0.5)]


def test_suggest_threshold():
    s = suggest('q', ['1234', '5678'], threshold=0.0)
    assert len(list(s)) == 2


def test_suggest_strategy():
    s = suggest('dna', ['dnaqb', 'dan'], strategy=relevance)
    assert len(list(s)) == 1


def test_extract():
    s = suggest('q', ['q1', 'q234'], threshold=0.2)
    assert extract(s) == [('q1', 0.5), ('q234', 0.25)]
    assert extract(s, limit=0) == []


def test_best_of():
    s = suggest('q', ['q1', 'q23'])
    assert best_of(s) == ('q1', 0.5)


def test_relative_best():
    s = suggest('q', ['q1', 'q234', ''], threshold=0.0)
    s = relative_best(s)
    assert extract(s) == [('q1', 0.5), ('q234', 0.25)]
