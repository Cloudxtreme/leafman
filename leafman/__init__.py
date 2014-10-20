from heapq import nlargest
from operator import itemgetter
from leafman.strategy import jaccard


def suggest(query, choices, threshold=0.5, strategy=jaccard):
    for choice in choices:
        rank = strategy(query, choice)
        if rank >= threshold:
            yield choice, rank


def extract(suggestions, limit=5):
    return nlargest(
        limit, suggestions,
        key=itemgetter(1),
    )
