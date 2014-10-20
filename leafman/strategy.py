"""
    leafman.strategy
    ~~~~~~~~~~~~~~~~
    Implements two strategies- the jaccard index and
    a relevancy-based index.
"""


def jaccard(query, value):
    """
    Performs the jaccard index on two given iterables,
    returning 0 if one of them is empty.

    :param query: The first iterable.
    :param value: Another iterable.
    """
    query, value = set(query), set(value)
    if not (query or value):
        return 0.0
    inter = len(query & value)
    union = len(query | value)
    return inter / float(union)


def relevance(query, value):
    """
    Performs relevance index on two iterables.

    :param query: The first iterable.
    :param value: Another iterable.
    """
    length = len(value)
    if not length or len(query) > length:
        return 0.0
    value, matches = iter(value), 0
    for char in query:
        for item in value:
            if item == char:
                matches += 1
                break
    return matches / float(length)
