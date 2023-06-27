#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """_summary_

    Args:
        obj (_type_): _description_
    """
    return obj.__dict__
