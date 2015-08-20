from __future__ import division
from .trie import Trie


def jaccard(query):
    query = set(query)
    length = len(query)

    def func(value):
        if not value:
            return 0.0
        value = set(value)
        inter = len(value & query)
        union = len(value) + length - inter
        return inter / union
    return func


def suggest(query, choices, metric=jaccard, threshold=0.3):
    metric = metric(query)
    for item in Trie(choices).get(query):
        score = metric(item)
        if score >= threshold:
            yield item, score
