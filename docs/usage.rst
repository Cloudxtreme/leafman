Usage
=====

###########
Basic Usage
###########

Usage of leafman is very simple- just use the
:func:`leafman.suggest` function:

.. code-block:: python

    from leafman import suggest
    suggestions = suggest(
        'bost',
        choices=[
            'boston',
            'houston',
            'denver',
        ]
    )

.. IMPORTANT::

    Do not pass empty queries to the :func:`leafman.suggest`
    function. This will cause some strategies
    to explode due to :class:`ZeroDivisionError`.


The :func:`leafman.suggest` function returns
an iterable that yields the choice, and a rank
for that choice, in the order that the choices
were given in. Note that it only yields the
choices with a rank equal or above 0.5 (50%).
To sort the suggestions it is recommended that
you use the :func:`leafman.process.extract`
function, for example:

.. code-block:: python

    from leafman.process import extract
    the_best = extract(suggestions, limit=5)

Often you will find that you need different
thresholds for ranks the of the suggestions.
You can configure this via the ``threshold``
parameter to the :func:`leafman.suggest` function:

.. code-block:: python

    suggest(
        'bost',
        choices=[],
        threshold=0.3,
    )

You can also change the strategy used; for
fuzzy searching of files for example you
can obtain Ctrl-P like behaviour if you use
the :func:`leafman.strategy.relevance`
strategy instead of the default
:func:`leafman.strategy.jaccard`. To change
the strategy pass the function as the ``strategy``
parameter:

.. code-block:: python

    from leafman.strategy import relevance
    suggest('bost', choices=[], strategy=relevance)

To extract the best suggestion you should
use the :func:`leafman.process.best_of`
function. For example:

.. code-block:: python

    from leafman.process import best_of
    assert best_of(the_best)[0] == 'boston'

Note that this function, along with the
:func:`leafman.process.extract` function
can work with any iterable that yields a
two-value tuple of choice and a rank.

You can also extract the relatively (above
or equal to the average) good suggestions
via the :func:`leafman.process.relative_best`
function. For example:

.. code-block:: python

    from leafman.process import relative_best
    relative_best(suggest(
        'query',
        choices=['query1', 'query2'],
    ))


##############
Advanced Usage
##############


~~~~~~~~~~~~~~~~~~~~~~~~~
Writing your own Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~

A strategy is a function that receives the
query value, and returns a closure that can
calculate a numerical rank based on a given
choice. This system is used because usually
you would want to cache some expensive
initial calculations that are performed on
the query value. For example, to write a simple
in-substring-or-not strategy:

.. code-block:: python

    def substring(query):
        def rank(value):
            return 1.0 if query in value else 0.0
        return rank

You can also write a class, because calling
classes is just like calling functions. For
example, the previous strategy but just wrapped
in a class:

.. code-block:: python

    class SubstringStrategy(object):
        def __init__(self, query):
            self.query = query

        def __call__(self, value):
            return 1.0 if query in value else 0.0

And then you can simply pass the strategy function
or class to the :func:`leafman.suggest` function,
in the ``strategy`` parameter:

.. code-block:: python

    suggest('query', choices=[], strategy=substring)
    suggest('query', choices=[], strategy=SubstringStrategy)


~~~~~~~~~~~~~~~~~~~~~
Preprocessing Pattern
~~~~~~~~~~~~~~~~~~~~~

For more expensive indexing strategies and situations
where the query changes but the choices do not, the
**Preprocessing Pattern** is preferred, for example:


.. code-block:: python

    class Strategy():
        def __init__(self):
            self.cache = {}

        def preprocess(self, iterable):
            for item in iterable:
                self.cache[item] = process(item)

        @property
        def choices(self):
            for item in self.cache:
                yield item

        def index(self, query):
            def closure(value):
                value = self.cache[value]
                return ratio(query, value)

And you can use this API very easily:

.. code-block:: python

    ins = Strategy()
    ins.preprocess(['query1', 'query2'])
    suggest('query', ins.choices, strategy=ins.index)

Though you are not required to follow this pattern
exactly, it is best if you do because it will make
it easier for the client code to swap out strategies
while keeping the method calls constant. However, if
you need to derive from the spec a little bit just
to make some performance-related tweaks, feel free
to do so.
