#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''Computes the set of elements present only in one set
    Args:
        set_1: first set
        set_2: second set
    Returns:
        The set of elements present only in on set
    '''
    c_set = set_1 ^ set_2
    return (c_set)
