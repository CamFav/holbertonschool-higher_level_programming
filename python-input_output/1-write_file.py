#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
