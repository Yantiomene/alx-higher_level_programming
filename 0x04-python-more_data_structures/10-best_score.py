#!/usr/bin/python3
def best_score(a_dictionary):
    '''Returns the key of the biggest integer value'''
    if not a_dictionary:
        return (None)
    maxi = max(a_dictionary.values())
    for key, v in a_dictionary.items():
        if v == maxi:
            return (key)
