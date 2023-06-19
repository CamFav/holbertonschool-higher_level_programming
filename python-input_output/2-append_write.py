#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
