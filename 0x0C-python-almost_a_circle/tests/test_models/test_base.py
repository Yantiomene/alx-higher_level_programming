#!/usr/bin/python3
"""Package for test cases"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestBaseMethods(unittest.TestCase):
    """Test case for Base class methods"""

    def setUp(self):
        """SetUp test method"""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """Test the default id"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id(self):
        """Test the id with int"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_multiple_id(self):
        """test id with multiple class instance"""
        new = Base()
        new2 = Base()
        new3 = Base(98)
        new4 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 98)
        self.assertEqual(new4.id, 3)

    def test_id_string(self):
        """ Test string id"""
        new = Base("1")
        self.assertEqual(new.id, "1")

    def test_2_args_id(self):
        """Test 2 args id for init method"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attr(self):
        """Test accessing the private attr"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_to_json_string(self):
        """ Test Dictionary to JSON string """
        r = Rectangle(2, 2)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(json_dictionary)
            self.assertEqual(std_out.getvalue(), res.replace("'", "\""))
