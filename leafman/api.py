from .trie import Trie
from .scoring import jaccard


def suggest(query, words, metric=jaccard, threshold=0.3):
    for item in Trie(words).get(query):
        score = metric(query, item)
        if score >= threshold:
            yield item, score
