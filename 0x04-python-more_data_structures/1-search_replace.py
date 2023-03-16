#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replaced_list = my_list[:]
    replaced_list[search - 1] = replace
    return replaced_list
