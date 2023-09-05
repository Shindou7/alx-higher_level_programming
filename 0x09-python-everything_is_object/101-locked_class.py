#!/usr/bin/python3


class LockedClass:
    """
    Prevent the user from creating a new instance dynamically
    except for the 'first_name' attribute.
    """
    __slots__ = "first_name"
