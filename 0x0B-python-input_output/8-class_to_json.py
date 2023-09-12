#!/usr/bin/python3
"""
Module 8-class_to_json.py
Write a function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """
    returns the dictionary description
    with a simple data structure
    """
    return obj.__dict__
