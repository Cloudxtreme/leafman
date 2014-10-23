from leafman.strategy import jaccard, relevance


def test_jaccard():
    jacc = jaccard('abb')
    assert jacc('abbbbb') == 1.0
    assert jacc('ab') == 1.0
    assert jacc('aaa') == 0.5
    assert jacc('adc') == 0.25
    assert jacc('') == 0.0


def test_relevance():
    relv = relevance('ab')
    assert relv('ab') == 1.0
    assert relv('abcd') == 0.5
    assert relv('acbd') == 0.5
    assert relv('abcdefgh') == 0.25
    assert relv('addd') == 0.0
    assert relv('') == 0.0
