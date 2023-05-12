#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ''' add 2 tuple and return the value
    args:
        tuple_a: first tuple
        tuple_b: second tuple
    Retuns:
        return the sum of the 2 tuple
    '''
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 0:
        if b == 0:
            return (0, 0)
        if b == 1:
            return (tuple_b[0], 0)
        return (tuple_b[0], tuple_b[1])

    if a == 1:
        if b == 0:
            return (tuple_a[0], 0)
        if b == 1:
            return (tuple_a[0] + tuple_b[0], 0)
        return (tuple_a[0] + tuple_b[0], tuple_b[1])

    if b == 0:
        return (tuple_a[0], tuple_a[1])
    if b == 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
