#!/usr/bin/python3
"""
Module  1-write_file.py
writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """
    Function that writes to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
