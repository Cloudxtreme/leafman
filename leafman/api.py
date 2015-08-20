from __future__ import division
import math
from .trie import Trie


def length_index(query):
    l1 = len(query)
    m1 = math.log10(l1)

    def score(value):
        if not value:
            return 0.0
        l2 = len(value)
        m2 = math.log10(l2)
        if int(m2) > int(m1):
            return math.pow(l1, m2 - m1) / l2
        return l1 / l2
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
