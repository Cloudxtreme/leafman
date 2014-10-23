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

    :param query: An initial query value.
    """
    query = set(query)
    length = len(query)

    def rank(value):
        if not value:
            return 0.0
        value = set(value)
        inter = len(query & value)
        union = len(value) + length - inter
        return inter / float(union)
    return rank


def relevance(query):
    """
    Returns a closure that performs relevance index
    a given iterable. A relevance index works like
    the Ctrl-P plugin for Vim- the characters within
    the query all need to be present in a given
    choice, in the same order.

    :param query: An initial query value.
    """
    query_length = len(query)

    def rank(value):
        length = len(value)
        if not length or length < query_length:
            return 0.0
        start = 0
        for char in query:
            idx = value.find(char, start)
            if idx == -1:
                return 0.0
            start = idx + 1
        return query_length / float(length)
    return rank
