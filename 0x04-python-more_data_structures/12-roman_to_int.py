#!/usr/bin/python3

def roman_to_int(roman_string):
    total = []
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            total.append(roman_numerals[roman_string[i]])
            break
        if roman_numerals[roman_string[i]] >= roman_numerals[roman_string[i + 1]]:
            total.append(roman_numerals[roman_string[i]])
        else:
            total.append(roman_numerals[roman_string[i]] * -1)

    return sum(total)
