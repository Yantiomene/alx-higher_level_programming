#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ''' Delete item at a specific position in a list
    args:
        my_list: list of number
        idx: position at which to delete item
    Returns:
        the new list
    '''
    n = len(my_list)
    if idx < 0 or idx >= n:
        return (my_list)
    del my_list[idx]
    return (my_list)
