#!/usr/bin/python3
def print_last_digit(number):
    '''return the last digit of a number'''
    if number >= 0:
        r = number % 10
    else:
        r = (-1 * number) % 10
    print(r, end="")
    return r
