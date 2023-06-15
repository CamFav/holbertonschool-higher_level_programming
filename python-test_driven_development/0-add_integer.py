#!/usr/bin/python3
"""Integers addition."""


def add_integer(a, b=98):
    """Add two integers."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or float")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
