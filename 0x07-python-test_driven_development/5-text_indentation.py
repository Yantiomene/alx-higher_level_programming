#!/usr/bin/python3

"""
Defines a function to print a text
with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """
      prints a text with 2 new lines after
      ., ?, and :
      Args:
          text: str
      Returns:
             None
    """

    char = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_cpy = text[:]

    for c in char:
        list_word = text_cpy.split(c)
        text_cpy = ""
        for w in list_word:
            w = w.strip(" ")
            if text_cpy == "":
                text_cpy = w + c
            else:
                text_cpy += "\n\n" + w + c

    print(text_cpy[:-3], end="")
