"""
    leafman.strategy
    ~~~~~~~~~~~~~~~~
    Implements two strategies- the jaccard index and
    a relevancy-based index.
"""


def jaccard(query):
    """
    Returns a closure that performs the jaccard index
    on a given iterable, taking the *query* into
    account.

    :param query: The first iterable.
    """
    length = len(query)

    def rank(value):
        if not (value or query):
            return 0.0
        inter = sum(1 for a in query if a in value)
        union = len(value) + length - inter
        return inter / float(union)
    return rank


def relevance(query):
    """
    Returns a closure that performs relevance index
    a given iterable.

    :param query: The first iterable.
    """
    query_length = len(query)

    def rank(value):
        length = len(value)
        if not length or query_length > length:
            return 0.0
        start = 0
        match = 0
        for char in query:
            idx = value.find(char, start)
            if idx == -1:
                return 0.0
            match += 1
            start = idx + 1
        return match / float(length)
    return rank
