#!/usr/bin/python3
"""This module returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """This functionreturns an object (Python data structure)
     represented by a JSON string"""
    from_str = json.loads(my_str)
    return from_str
