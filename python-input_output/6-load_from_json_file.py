#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    with open(filename, "r") as file:
        return json.load(file)
