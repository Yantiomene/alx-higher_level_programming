#!/usr/bin/python3
def safe_print_integer(value):
    '''Safe print an integer'''
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (False)
    else:
        return (True)
