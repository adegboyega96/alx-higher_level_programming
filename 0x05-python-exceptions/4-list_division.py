#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_length = []
    for i in range(max(len(my_l_1), len(my_l_2))):
        try:
            result = my_list_1[i]/my_list_2[i]
            list_length.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            list_length.append(result)
        except TypeError:
            print("wrong type")
            result = 0
            list_length.append(result)
        except IndexError:
            print("out of range")
            result = 0
            list_length.append(result)
    return list_length
