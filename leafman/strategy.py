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
    query = set(query)

    def rank(value):
        value = set(value)
        if not (value or query):
            return 0.0
        inter = len(query & value)
        union = len(query | value)
        return inter / float(union)
    return rank


def relevance(query):
    """
    Returns a closure that performs relevance index
    a given iterable.

    :param query: The first iterable.
    """
    query_length = len(query)
    fql = float(query_length)

    def rank(value):
        length = len(value)
        if not length or query_length > length:
            return 0.0
        start = 0
        match = 0
        for char in query:
            idx = value.find(char, start)
            if idx == -1:
                break
            match += 1
            start = idx + 1
        return match / fql
    return rank
