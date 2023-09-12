#!/usr/bin/python3
"""
Module 4-from_json_string.py
function that returns an objec JSON representation
"""
import json


def from_json_string(my_str):
    """
    returns an object by a JSON representation
    """
    return json.loads(my_str)
