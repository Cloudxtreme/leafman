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


def build_engine(finder, metric):
    def function(query):
        score = metric(query)
        for item in finder.get(query):
            yield item, score(item)
    return function


def suggest(query, choices, finder=Trie, metric=jaccard):
    engine = build_engine(finder(choices), metric)
    return engine(query)
