
Exponentiation
==============

Here are the exponentiation/quadratic related functions.
they are unstable at the moment, but works well in expected situations.

``xpnt(arg=[0])``
    exponentiation operation. it can do it recursively, like:

    .. code-block:: python

        from Matematica import xpnt

        x = xpnt([2, 2, 2])
        print(x)

    **output:**

    .. code-block::

        16

    here 2 is raised to the power of 2 and then the result is raised to the power of 2.
    If only one value is given, it will raise it to the power of 2, as in:

    .. code-block:: python

        from Matematica import xpnt

        x = xpnt([3])
        print(x)

    **output:**

    .. code-block::

        9

    Note that you can work with lists just like the `basic operators`_.


``nRoot(arg0=1, arg1=2)``
    gets the 'n' root of a number, as in 'a square root'(witch is default when only the first argument is given).

    sample:

    .. code-block:: python

        from Matematica import nRoot

        x = nRoot(8, 3)
        print(x)

    **output:**

    .. code-block::

        2.0

    Note the floating point. nRoot() has a floating point precision of 1, see an example:

    .. code-block:: python

        from Matematica import nRoot

        x = nRoot(10)
        print(x)

    **output:**

    .. code-block::

        3.1

``qdeq(a, b, c)``
    solves a simple quadratic equation and returns a tuple with the results.
    the first item is the '+' version of the formula, and the second is the '-' version.
    if the discriminant is negative, it returns ``False``

``qdeqDisc(a, b, c)``
    calculates the discriminant for the quadratic formula.

_`basic operators`: #
