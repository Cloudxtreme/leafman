.. Leafman documentation master file, created by
   sphinx-quickstart on Wed Oct 22 22:54:53 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Leafman
=======

Leafman is a very simple and fast library for generating
suggestions. It is based by default on the Jaccard index,
but it's intuitive design will make using any indexing
strategy a breeze.

.. code-block:: python

    from leafman import suggest
    suggest('query', ['choice1', 'choice2'])

Due to the emphasis on simiplicity, speed, and composability,
and the domain of the problem, Leafman uses a functional style,
similar to that of the ``heapq`` library. To install just do a
``pip install leafman``.


.. toctree::
   :maxdepth: 2

   intro
   usage
   api
