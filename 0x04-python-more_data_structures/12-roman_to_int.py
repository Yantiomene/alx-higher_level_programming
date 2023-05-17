#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Convert a roman string to integer'''
    roman_int = {
        'I': 1, 'IV': 4,
        'V': 5, 'IX': 9,
        'X': 10, 'XL': 40,
        'L': 50, 'XC': 90,
        'C': 100, 'CD': 400,
        'D': 500, 'CM': 900,
        'M': 1000
        }
    if not roman_string or (not isinstance(roman_string, str)):
        return (0)
    num = 0
    i = 0
    while i < len(roman_string):
        if (i < len(roman_string) - 1) and roman_string[i:i+2] in roman_int:
            num += roman_int[roman_string[i:i+2]]
            i += 2
        elif roman_string[i] in roman_int:
            num += roman_int[roman_string[i]]
            i += 1

    return (num)
