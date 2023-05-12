#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0 or idx >= n:
        return (my_list)
    list_cpy = my_list[:]
    list_cpy[idx] = element
    return (list_cpy)
