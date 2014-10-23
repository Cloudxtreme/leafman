Introduction
============

Leafman is a very simple and fast suggestion library.
It can be used for multiple purposes, such as:

- fuzzy searching
- correcting typos


############
Installation
############

In general you would want to pick up the latest stable
version, which is ``0.1.3``, from PyPI:

.. code-block:: sh

    $ pip install leafman==0.1.3

However if you'd like to contribute to development or
use the latest builds, it is recommended that you clone
the repository via git:

.. code-block:: sh

    $ git clone https://github.com/eugene-eeo/leafman


##########
Philosophy
##########

There are already many packages that provide fuzzy
string matching, such as the excellent ``fuzzywuzzy``.
The aim of Leafman is not to replace those tools, but
to establish a common API that can be plugged in by
those tools. Leafman also aims to be simple, and
composable. Also, since suggestions should happen
typically in an instant, we also want the library to
be fast.
