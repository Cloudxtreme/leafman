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
        choice and returns a number.
    """
    for choice in choices:
        rank = strategy(query, choice)
        if rank >= threshold:
            yield choice, rank


def extract(suggestions, limit=5):
    """
    Extract the best choices from *suggestions*
    and only give the best *limit* ones.

    :param suggestions: An iterable of suggestions.
    :param limit: Defaults to 5.
    """
    return nlargest(
        limit, suggestions,
        key=itemgetter(1),
    )


def best_of(suggestions):
    """
    Returns the best suggestion out of
    *suggestions*.

    :param suggestions: An iterable of suggestions.
    """
    return max(suggestions, key=itemgetter(1))
