#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Add unique integers in a list
    Args:
        my_list: list of integers
    Returns:
        the sum
    '''
    summ = sum(set(my_list))
    return (summ)
