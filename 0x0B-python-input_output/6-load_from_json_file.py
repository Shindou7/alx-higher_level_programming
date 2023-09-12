#!/usr/bin/python3
""" Module 6-load_from_json_file.py
creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Function that Creates a Python obj from JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
