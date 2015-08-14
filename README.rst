.. image:: https://raw.github.com/eugene-eeo/leafman/master/art/banner.png

Leafman is a very small, fast, and simple autocompletion
library for Python. It defaults to using a trie to generate
suggestions, but the suggestion generation is pluggable:

.. code-block:: python

    >>> from leafman import suggest
    >>> list(suggest('abc', ['abcd', 'abcdef']))
    [('abcd', 0.75), ('abcdef', 0.5)]

.. _documentation: http://leafman.readthedocs.org/
