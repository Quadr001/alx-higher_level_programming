#!/usr/bin/python3

"""This defines an object attribute lookup function."""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: list of available attributes and
                 methods of an object
    """
    return dir(obj)
