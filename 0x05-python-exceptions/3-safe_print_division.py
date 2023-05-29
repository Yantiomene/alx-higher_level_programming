#!/usr/bin/python3
def safe_print_division(a, b):
    ''' Divides 2 integrers and prins the result'''
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))

    return (quotient)
