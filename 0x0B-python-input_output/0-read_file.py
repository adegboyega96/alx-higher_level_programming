#!/usr/bin/python3
"""Text reading module from a file"""


def read_file(filename=""):
    """Prints the contents insde the text file"""
    with open(filename, encoding="utf-8") as data:
        print(data.read())
