#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Find all multiples of 2 in a list
    args:
        my_list: list of number
    Returns:
        a list of boolean containing True if multiple of 2
    '''
    multi_2 = []
    for i in my_list:
        if i % 2 == 0:
            multi_2.append(True)
        else:
            multi_2.append(False)

    return (multi_2)
