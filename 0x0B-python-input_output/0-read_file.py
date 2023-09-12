#!/usr/bin/python3
"""
Module 0-read_file.py
Function that reads from a file
"""


def read_file(filename=""):
    """Function that reads and print from a file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
