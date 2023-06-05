#!/usr/bin/python3

""" Defines a function to multiply
    2 matrices using numpy library
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices
       Args:
           m_a: first matrix
           m_b: second matrix
       Returns: the product of the 2 matrices
    """

    return np.matmul(m_a, m_b)
