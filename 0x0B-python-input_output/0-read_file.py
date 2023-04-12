#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, encoding="utf-8") as data:
        read_data = data.read()
        print(read_data)
