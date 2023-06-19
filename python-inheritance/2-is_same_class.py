#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    return type(obj) is a_class
