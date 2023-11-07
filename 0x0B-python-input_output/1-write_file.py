#!/usr/bin/python3
"""
function that write a string to text (UTF8) and
return total of the character written
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
