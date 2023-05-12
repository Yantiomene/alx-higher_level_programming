#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return (None)
    maxi = my_list[0]
    for i in my_list[1:]:
        if i > maxi:
            maxi = i
    return (maxi)
