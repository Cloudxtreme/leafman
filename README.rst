.. image:: https://raw.github.com/eugene-eeo/leafman/master/art/banner.png

Leafman is a very small, straightforward, and fast
library for computing suggestions based on a given
string and choices. It is based (by default) on the
Jaccard index, though any comparing function can be
used.

.. code-block:: python

    >>> from leafman import suggest
    >>> list(suggest('abc', ['abcd', 'abcdef', 'adede']))
    [('abcd', 0.75), ('abcdef', 0.5)]

Due to the emphasis on simiplicity, speed, and
composability, and the domain of the problem,
Leafman uses a functional style, similar to that
of the ``heapq`` library. To install just do a
``pip install leafman``. To find out more you can
read the `documentation`_.

.. _documentation: http://leafman.readthedocs.org/
