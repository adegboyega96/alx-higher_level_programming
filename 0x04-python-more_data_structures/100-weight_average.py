#!/usr/bin/python3

def mul(my_tuples):
    total = 1
    for i in my_tuples:
        total *= i
    return total


def weight_average(my_list=[]):
    total = 0
    div = []
    for tuples in my_list:
        total += mul(tuples)
        div.append(tuples[1])
    return total/sum(div)
