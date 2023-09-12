#!/usr/bin/python3
"""
Module 2-append_write.py
appends to text file and returns num chars added
"""


def append_write(filename="", text=""):
    """
    Function that appends to a text file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
