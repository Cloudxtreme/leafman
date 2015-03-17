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
    suggested = []
    runsum = 0

    for choice, rank in suggestions:
        suggested.append((choice, rank))
        runsum += rank

    return suggested, runsum


def relative_best(suggestions):
    """
    Returns the best suggestions relatively, that
    is that their ranking equals or exceeds that of
    the average ranking.

    :param suggestions: The suggestions.
    """
    suggested, runsum = _sum_ranks(suggestions)
    if not suggested:
        return

    average = float(runsum) / len(suggested)
    for choice, rank in suggested:
        if rank >= average:
            yield choice, rank
