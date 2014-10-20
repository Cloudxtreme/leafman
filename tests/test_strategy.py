from leafman.strategy import jaccard, relevance


def test_jaccard():
    assert jaccard('ab', 'ab') == 1.0
    assert jaccard('ab', 'a') == 0.5
    assert jaccard('ab', '') == 0.0


def test_relevance():
    assert relevance('ab', '') == 0.0
    assert relevance('dna', 'dqab') == 0.25
    assert relevance('query', 'query') == 1.0
