from __future__ import division
from .trie import Trie


def jaccard(a, b):
    a = set(a)
    b = set(b)
    return len(a & b) / len(a | b)


def suggest(query, choices, metric=jaccard, threshold=0.3):
    for item in Trie(choices).get(query):
        score = metric(query, item)
        if score >= threshold:
            yield item, score
