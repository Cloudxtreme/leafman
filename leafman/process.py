"""
    leafman.process
    ~~~~~~~~~~~~~~~
    Functions for utilising the various strategies to
    compute suggestions.
"""


from heapq import nlargest
from operator import itemgetter
from leafman.strategy import jaccard


def suggest(query, choices, threshold=0.5, strategy=jaccard):
    """
    Return an iterable of choice to distance pairs
    which distances from the *query* are above or
    equal to the given *threshold*.

    :param query: The query.
    :param choices: An iterable of choices.
    :param threshold: Inclusive minimum bound.
    :param strategy: Defaults to ``jaccard``; can
        be any function that takes a query and
        returns a closure, that calculates an
        index.
    """
    meth = strategy(query)
    for choice in choices:
        rank = meth(choice)
        if rank >= threshold:
            yield choice, rank


def extract(suggestions, limit=5):
    """
    Extract the best choices from *suggestions* and
    only give up to *limit* choices.

    :param suggestions: An iterable of suggestions.
    :param limit: Defaults to 5.
    """
    rank = itemgetter(1)
    return (
        [max(suggestions, key=rank)] if limit == 1 else
        nlargest(limit, suggestions, key=rank)
        )


def _sum_ranks(suggestions):
    """
    Sum the ranks of given *suggestions* then
    returns a new, copied list of suggestions,
    the summation, and the size.

    :param suggestions: An iterable of suggestions.
    """
    suggested = []
    runsum = 0
    size = 0

    for size, datum in enumerate(suggestions, 1):
        suggested.append(datum)
        runsum += datum[1]

    return suggested, runsum, size


def relative_best(suggestions):
    """
    Returns the best suggestions relatively, that
    is that their ranking equals or exceeds that of
    the average ranking.

    :param suggestions: The suggestions.
    """
    suggestions, runsum, size = _sum_ranks(suggestions)
    if size:
        average = float(runsum) / size
        for choice, rank in suggestions:
            if rank >= average:
                yield choice, rank
