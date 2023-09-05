#!/usr/bin/python3
"""
Module 5-text_indentation
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", , ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]
    result = ""
    new_line = True

    for char in text:
        if char in separators:
            result += char + "\n\n"
            new_line = True
        elif char != " ":
            if new_line:
                result += char
                new_line = False
            else:
                result += char

    print(result, end="")
