=====
Ropes
=====

Basic implementation of a rope-based string in Python.


About ropes
===========

Ropes are an mutable alternative to strings.  The string is represented as a
binary tree, and modifications to the string are achieved by either replacing
existing substring branches or by inserting new substrings into the tree
structure.

This is a very simple implementation which supports the basic operations, such
as concatenation, indexing, slices, and strides.

There has been little attention to performance, particularly related to the
dynamic rebalancing of the tree, which is one of the main reasons to ever
consider using a rope, so this is more for demonstration purposes than for use
in production.

Having said that, I am happy with the API and integration with intrinsic Python
syntax, and there is certainly opportunity for improving the implementation of
the internal tree.


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
