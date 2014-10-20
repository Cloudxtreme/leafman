"""
    leafman.strategy
    ~~~~~~~~~~~~~~~~
    Implements two strategies- the jaccard index and
    a relevancy search.
"""


def jaccard(d1, d2):
    """
    Performs the jaccard index on two given iterables,
    returning 0 if one of them is empty.

    :param d1: The first iterable.
    :param d2: Another iterable.
    """
    d1, d2 = set(d1), set(d2)
    if not (d1 or d2):
        return 0.0
    inter = len(d1 & d2)
    union = len(d1 | d2)
    return inter / float(union)


def relevance(d1, d2):
    """
    Performs relevance index on two iterables.

    :param d1: The first iterable.
    :param d2: Another iterable.
    """
    length = len(d2)
    if not length or len(d1) > length:
        return 0.0
    d2, matches = iter(d2), 0
    for char in d1:
        for item in d2:
            if item == char:
                matches += 1
                break
    return matches / float(length)
