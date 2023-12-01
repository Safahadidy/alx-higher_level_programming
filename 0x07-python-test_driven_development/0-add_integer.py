#!/usr/bin/python3
"""" add_two_integer """
def add_integer(a, b=98):
    """"
    args:
    a: ints or float
    b: ints or float
    returns:
    add a + b
    
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)