#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if a_class is type(obj):
        return False
    return issubclass(type(obj), a_class)
