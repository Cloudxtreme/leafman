leafman
=======

Leafman is a very straightforward and fast library
for computing suggestions based on a given string,
and choices. It is based internally on the Jaccard
index, though any ranking function can be used.

```python
from leafman import suggest
suggest(query, [choices])
```
