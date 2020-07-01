
Operators
=========

Here you will see how easy and handy it is to work with the basic operators.

``add(arg=[0])``
    Add a n number of numbers

``subtract(arg=[0])``
    Subtract a n number of numbers

``multiply(arg=[0])``
    Multiply a n number of numbers

``divide(arg=[0])``
    Divide a n number of numbers

as you can see, they are really self explanatory.


Examples
--------

You can do all kind of things that involves lists, like list comprehensions:

.. code-block:: python

    import Matematica as mat

    x = mat.add([n for n in range(10)])
    print(x)

**output:**

.. code-block:: python

    45
