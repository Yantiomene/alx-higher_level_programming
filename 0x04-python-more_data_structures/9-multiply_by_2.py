#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''Multiply all value of a dict by 2
    Args:
        a_dictionary: a dictionary
    Returns:
        A new dict with value multiply by 2
    '''
    dict_m_2 = {}
    for key, v in a_dictionary.items():
        dict_m_2[key] = v * 2

    return (dict_m_2)
