#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' Prints x elements of my_list'''
    count = 0
    for i in range(x):
        try:
            val = my_list[i]
        except IndexError:
            break
        else:
            print(val, end="")
            count += 1
    print()
    return (count)
