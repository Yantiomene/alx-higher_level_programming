#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Returns the weighted average of all integers tuple'''
    if not my_list:
        return (0)
    w_avg = sum([x[0] * x[1] for x in my_list]) / sum([x[1] for x in my_list])
    return (w_avg)
