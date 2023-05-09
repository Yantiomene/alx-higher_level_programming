#!/usr/bin/python3
def remove_char_at(str, n):
    ''' Remove the char in str at position n and return the new string'''
    str_cpy = ""
    for i in range(len(str)):
        if i != n:
            str_cpy += str[i]

    return (str_cpy)
