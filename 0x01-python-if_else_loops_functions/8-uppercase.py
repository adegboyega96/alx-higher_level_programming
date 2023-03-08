#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if 96 < j < 123:
            j -= 32
        print(chr(j), end='')
