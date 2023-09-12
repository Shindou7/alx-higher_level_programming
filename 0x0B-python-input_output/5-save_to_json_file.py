#!/usr/bin/python3
""" Module 5-save_to_json_file.py
writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes Python obj to file using JSON represenation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
