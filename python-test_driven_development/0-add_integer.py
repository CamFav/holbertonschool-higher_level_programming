#!/usr/bin/python3
"""Integers addition."""


def add_integer(a, b=98):
    """Add two integers."""
    try:
        result = a + b
        return int(result)
    except TypeError:
        if type(a) not in [int, float]:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
