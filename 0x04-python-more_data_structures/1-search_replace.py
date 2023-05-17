#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Replaces all occurrences of an element
    Args:
        my_list: initial list
        search: is the element to be replace in the list
        replace: is the new element
    Returns:
        a new list
    '''
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return (new_list)
