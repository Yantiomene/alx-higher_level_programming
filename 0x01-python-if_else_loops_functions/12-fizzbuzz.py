#!/usr/bin/python3
def fizzbuzz():
    '''Prints number from 1 to 100 separated by space
    - Prints Fizz for multiple of 3
    - Prints Buzz for multiple of 5
    - Prints FizzBuzz for multiple of both 3 and 5'''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
