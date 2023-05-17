#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''COmpute the common elements of 2 sets
    Args:
        set_1: first set
        set_2: second set
    Returns:
        set of common elements
    '''
    c_set = set_1 & set_2
    return (c_set)
