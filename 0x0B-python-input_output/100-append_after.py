#!/usr/bin/python3
"""
Module 100-append_after.py
that executes a function that appends a line
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that appends a new line when a string is found
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_write= ""
        for line in f:
            new_write += line
            if search_string in line:
                new_write += new_string
        f.seek(0)
        f.write(new_write)
