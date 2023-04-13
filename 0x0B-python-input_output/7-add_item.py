#!/usr/bin/python3
"""This module adds all argumes to a python list
and then save to a file """
import sys

if __name__ == "__main__":
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    try:
        lst = load_from_json_file(filename)
        for arg in sys.argv[1:]:
            lst.append(arg)
        save_to_json_file(lst, filename)
    except FileNotFoundError:
        lst = []
        for arg in sys.argv[1:]:
            lst.append(arg)
        save_to_json_file(lst, filename)
