#!/usr/bin/python3

def roman_to_int(roman_string):
    total = []
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            total.append(digits[roman_string[i]])
            break
        if digits[roman_string[i]] >= digits[roman_string[i + 1]]:
            total.append(digits[roman_string[i]])
        else:
            total.append(digits[roman_string[i]] * -1)
