def jaccard(d1, d2):
    d1, d2 = set(d1), set(d2)
    if not (d1 or d2):
        return 0.0
    inter = d1.intersection(d2)
    union = d1.union(d2)
    return len(inter) / float(len(union))


def relevance(d1, d2):
    length = len(d2)
    if not length or length < len(d1):
        return 0.0
    d2, acc = iter(d2), 0
    for item in d1:
        for q in d2:
            if q == item:
                acc += 1
                break
    return acc / float(length)
