
Utilities
=========

Here are some tools that make things nicer.

``fract(arg)``
    turns a decimal into a fraction. Example:

    .. code-block:: python

        from Matematica import fract, divide

        y = divide([78, 7, 9, 5])
        x = fract(float(format(y, '.1f')))
        print(f"Before: {y}\nAfter: {x}")


    **output:**

    .. code-block:: python

        Before: 0.24761904761904763
        After: 1/5

    Note that it only works(for now) with 1 floating point precision.
