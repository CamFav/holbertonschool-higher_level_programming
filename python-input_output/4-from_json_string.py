#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """_summary_

    Args:
        my_str (_type_): _description_
    """
    return json.loads(my_str)
