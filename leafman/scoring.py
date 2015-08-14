from __future__ import division


def jaccard(a, b):
    a = set(a)
    b = set(b)
    return len(a & b) / len(a | b)
