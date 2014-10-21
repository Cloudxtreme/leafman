from leafman.strategy import jaccard, relevance


def test_jaccard():
    jacc = jaccard('ab')
    assert jacc('ab') == 1.0
    assert jacc('a') == 0.5
    assert jacc('') == 0.0


def test_relevance():
    relv = relevance('ab')
    assert relv('ab') == 1.0
    assert relv('dqab') == 0.50
    assert relv('') == 0.0
