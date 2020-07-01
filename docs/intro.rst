
Introduction
============

Matematica is a more pythonish simple and powerful python library.

.. code-block:: python

    import Matematica as mat

    x = mat.add([n for n in range(10)])
    print(x)

**output:**

.. code-block::

    45


Basic operators
---------------

I've re-created all 4 basic operators so you can easily manage them.

.. code-block:: python

    import Matematica as mat

    x = mat.divide([mat.multiply([4, 6, 9]), mat.subtract([2, 3, 4])])
    print(x)

**output:**

.. code-block::

    -43.2

It is really more convenient this way because you don't get confused within your code.

you can read more about them in Operators_


Quadratic operators
-------------------

You can do quadratic equations within square roots with recursive exponentiation,
and the best part is: IT'S HUMAN READABLE!

.. code-block:: python

    from Matematica import nRoot as r, qdeq as q, xpnt as x

    n = x([q(1, 3, 2)[1], x([r(8, 3), 10])])
    print(n)

**output:**

.. code-block::

    4294967296.0

you can see that it's easy to mix up things. There are some limitations though.
See more in Exponentiation_


Utilities
---------

There are some situations that you can get stuck on like when working with floats.

.. code-block:: python

    from Matematica import fract, divide

    y = divide([78, 7, 9, 5])
    x = fract(float(format(y, '.1f')))
    print(f"Before: {y}\nAfter: {x}")


**output:**

.. code-block::

    Before: 0.24761904761904763
    After: 1/5

there are some limitations though(for now). See more in Utilities_

Others
------

there are some useful but not categorized functions that you can find in Others_

.. _Operators: #
.. _Utilities: #
.. _Exponentiation: #
.. _Others: #
