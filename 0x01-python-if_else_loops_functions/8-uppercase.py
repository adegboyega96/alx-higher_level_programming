#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if 96 < j < 123:
            j -= 32
        new_str = chr(j)
        print('{}'.format(new_str), end='')
