#!/usr/bin/python3
"""Module that defines a function to add two integers."""

def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.
    
    Floats are cast to integers. Raises TypeError if a or b are not int/float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
