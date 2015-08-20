from collections import deque


def longest(tree):
    if tree is None:
        return
    q = deque([tree])
    while q:
        t = q.popleft()
        for k in t:
            if k is None:
                yield t[k]
                continue
            q.append(t[k])


class Trie(object):
    def __init__(self, data=()):
        self.tree = {}
        for item in data:
            self.insert(item)

    def insert(self, seq):
        t = self.tree
        for k in seq:
            if k not in t:
                t[k] = {}
            t = t[k]
        t[None] = seq

    def get(self, seq):
        t = self.tree
        for item in seq:
            if item not in t:
                return []
            t = t[item]
        return list(longest(t))
