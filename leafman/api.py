from .trie import Trie
from __future__ import division


def jaccard(a, b):
    a = set(a)
    b = set(b)
    return len(a & b) / len(a | b)


def suggest(query, words, metric=jaccard, threshold=0.3):
    for item in Trie(words).get(query):
        score = metric(query, item)
        if score >= threshold:
            yield item, score
