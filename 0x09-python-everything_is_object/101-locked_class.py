#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Allows only firstname attributes instatioation"""

    __slots__ = ["first_name"]
