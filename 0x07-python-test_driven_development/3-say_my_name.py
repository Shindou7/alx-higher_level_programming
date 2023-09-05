#!/usr/bin/python3
""" Module 3-say_my_name """


def say_my_name(first_name: str, last_name: str = "") -> None:
  """
  Prints "My name is [name]"
  """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
