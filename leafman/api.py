import math
from .trie import Trie


def length_index(query):
    l0 = len(query)

    def score(value):
        if not value:
            return 0
        return l0 / float(len(value))
    return score


def build_engine(finder, metric):
    def function(query):
        score = metric(query)
        for item in finder.get(query):
            yield item, score(item)
    return function


def suggest(query, choices, finder=Trie, metric=length_index):
    engine = build_engine(finder(choices), metric)
    return engine(query)
