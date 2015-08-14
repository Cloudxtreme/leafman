from .trie import Trie
from .scoring import jaccard


def fmap(funcs, item):
    for fn in funcs:
        item = fn(item)
    return item


def suggest(query, words, score=jaccard, threshold=0.3):
    pass
