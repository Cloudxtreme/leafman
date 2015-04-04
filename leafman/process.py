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


def _avg_ranks(suggestions):
    """
    Returns the average of the ranks for the given
    suggestions, and then returns a copied list of
    suggestions.

    :param suggestions: An iterable of suggestions.
    """
    suggested = []
    runsum, size = 0, 0

    for size, datum in enumerate(suggestions, 1):
        suggested.append(datum)
        runsum += datum[1]

    return (float(runsum) / size if suggested else 0,
            suggested)


def relative_best(suggestions):
    """
    Returns the best suggestions relatively, that
    is that their ranking equals or exceeds that of
    the average ranking.

    :param suggestions: The suggestions.
    """
    average, suggestions = _avg_ranks(suggestions)
    for choice, rank in suggestions:
        if rank >= average:
            yield choice, rank
