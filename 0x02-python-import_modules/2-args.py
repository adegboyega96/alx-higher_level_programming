#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

print("{} arguments.".format(num_arguments))
for arg in arguments:
    print("{}: {}".format((arguments.index(arg) + 1), arg))
