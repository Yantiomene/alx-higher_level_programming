#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function which finds a peak in a list
    Args:
        list_of_integers: List of unsorted integers
    Return:
        a peak
    """

    if list_of_integers == []:
        return None
    a_li = list_of_integers[:]
    n = len(a_li)
    mid = int(n / 2)

    if (mid - 1) == -1 and (mid + 1) == n:
        return a_li[mid]
    if (mid - 1) == -1:
        return a_li[mid] if a_li[mid] > a_li[mid + 1] else a_li[mid + 1]
    if (mid + 1) == n:
        return a_li[mid] if a_li[mid] > a_li[mid - 1] else a_li[mid - 1]

    if a_li[mid - 1] < a_li[mid] > a_li[mid + 1]:
        return a_li[mid]

    if a_li[mid + 1] > a_li[mid - 1]:
        return find_peak(a_li[mid:])
    return find_peak(a_li[:mid])
