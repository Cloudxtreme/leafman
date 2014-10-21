<img src="https://raw.github.com/eugene-eeo/leafman/master/art/logo.png" align="left" vspace="35">

# Leafman

Leafman is a very straightforward and fast library
for computing suggestions based on a given string,
and choices. It is based internally on the Jaccard
index, though any comparing function can be used.

```python
from leafman import suggest
suggest('query', ['choice1', 'choice2'])
```

Due to the emphasis on simiplicity, speed, and
composability, and the domain of the problem,
Leafman uses a functional style, similar to that
of the ``heapq`` library.
