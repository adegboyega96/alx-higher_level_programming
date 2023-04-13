#!/usr/bin/python3
"""This module return the json representation of an object
"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string"""
    to_str = json.dumps(my_obj)
    return to_str
