#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the function
       max_integer
    """

    def test_max_int(self):
        """list of integers test case
        """
        self.assertEqual(max_integer([2, 1, 4, 3]), 4)

    def test_repeat_int(self):
        """list with repeated number
        """
        self.assertEqual(max_integer([10, 10, 20, 20]), 20)

    def test_single_list(self):
        """List with only one element
        """
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_max_start(self):
        """max at the beginning of the list
        """
        self.assertEqual(max_integer([50, 30, 20, 0]), 50)

    def test_sorted_list(self):
        """sorted list
        """
        self.assertEqual(max_integer([-2, 4, 34, 200]), 200)

    def test_neg_int(self):
        """list with neg integer
        """
        self.assertEqual(max_integer([-2, -4, -1, -50, -3]), -1)

    def test_float_number(self):
        """list containing float
        """
        self.assertEqual(max_integer([50, 49.99, -3, 29.6, -100.567]), 50)

    def test_zero_list(self):
        """list with only zero
        """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_list_comp(self):
        """Comprehension list
        """
        self.assertEqual(max_integer([i * i for i in range(11)]), 100)

    def test_big_list(self):
        """big list
        """
        self.assertEqual(max_integer([
            99, 98, 97, 96, 95, 94, 93, 92, 91, 90,
            100, 900, 901, 902, 903, 904, 905, 906,
            907, 908, 909, 910, 1000, 911, 912, 913,
            914, 915, 916, 917, 918, 919, 920, 999,
            998, 98, 99, 997, 97, 996, 96, 995, 95]), 1000)

    def test_string_list(self):
        """list containing a string
        """
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3, '4'])

    def test_tuple(self):
        """tuple as list
        """
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_tuple_list(self):
        """list containing a tuple
        """
        with self.assertRaises(TypeError):
            max_integer([1, (2, 3), 4])

    def test_list_list(self):
        """list containing a list
        """
        with self.assertRaises(TypeError):
            max_integer([1, [2, 3], 4])

    def test_number(self):
        """passes a number as arg
        """
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_dict(self):
        """passes dict as arg
        """
        with self.assertRaises(KeyError):
            max_integer({'a': 1, 'b': 2})
