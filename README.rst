.. image:: https://raw.github.com/eugene-eeo/leafman/master/art/banner.png

Leafman is a very small, straightforward, and fast
library for computing suggestions based on a given
string and choices. It is based (by default) on the
Jaccard index, though any comparing function can be
used.

.. code-block:: python

    from leafman import suggest
    suggest('query', ['choice1', 'choice2'])

Due to the emphasis on simiplicity, speed, and
composability, and the domain of the problem,
Leafman uses a functional style, similar to that
of the ``heapq`` library. To install just do a
``pip install leafman``. To find out more you can
read the `documentation`_.

.. _docs: http://leafman.readthedocs.org/
