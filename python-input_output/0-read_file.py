#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        readfile = f.read()
    print(readfile, end="")
