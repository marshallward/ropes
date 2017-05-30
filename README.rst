=====
Ropes
=====

Early implementation of a Rope data structure in Python.


About ropes
===========

Ropes are an mutable alternative to strings.  The string is represented as a
binary tree, and modifications to the string are achieved by either replacing
existing substring branches or by inserting new substrings into the tree
structure.

This is a preliminary version which supports the basic operations, such as
concatentation, indexing, slices, and strides.

Implementation of some features is currently poor, particularly the slicing
operations.  No effort is made to balance the tree or otherwise optimise the
data structure.


Usage
=====

To convert a string into a rope, use the ``Rope`` class constructor.

.. code:: python

   r = Rope('abcdefg')

A pre-defined ``Rope`` tree can be constructed using a list of strings.

.. code:: python

   r = Rope(['abc', 'def', 'g'])

Printing the rope returns a string.

.. code:: python

   >>> r = Rope(['abc', 'defg'])
   >>> r
   (Rope('abcd') + Rope('efg'))
   >>> print(r)
   abcdefg

Strings can be inserted between existing ropes.

.. code:: python

   >>> r, s = Rope('abc'), Rope('def')
   >>> u = '123'
   >>> r + u + s
   ((Rope('abc') + Rope('123')) + Rope('def'))
   >>> print(r + u + s)
   abc123def
   >>>

Current usage is very basic, but will hopefully improve in the future.
