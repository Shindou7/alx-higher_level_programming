#!/usr/bin/python3
"""
Module 3-to_json_string.py
returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of obj (string)
    """
    return json.dumps(my_obj)
