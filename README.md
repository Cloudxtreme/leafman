Leafman
=======

<img src="http://raw.github.com/eugene-eeo/leafman/master/art/logo.png" align="left">

Leafman is a very straightforward and fast library
for computing suggestions based on a given string,
and choices. It is based internally on the Jaccard
index, though any comparing function can be used.

```python
from leafman import suggest
suggest('query', ['choice1', 'choice2'])
```

Due to the emphasis on simiplicity, speed and
composability, and the domain of the problem,
Leafman uses a functional style, similar to that
of the ``heapq`` library. You can easily extend
the Leafman library by writing your own strategy:

```python
def simple(query, choice):
    if not choice:
        return 0.0
    query, choice = set(query), set(choice)
    return len(query & choice) / float(len(choice))

suggest('boston',
        ['boston', 'arkansas'],
        strategy=simple)
```
