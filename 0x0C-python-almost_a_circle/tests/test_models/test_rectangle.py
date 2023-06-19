#!/usr/bin/python3
"""Test class for rectangle class methods"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethdods(unittest.TestCase):
    """Test suite for rectangke class methods"""

    def setUp(self):
        """setUp method"""
        Base._Base__nb_objects = 0

    def test_new_rect(self):
        """Test a new rectangle"""
        rtg = Rectangle(1, 1, 1, 1, 98)
        self.assertEqual(rtg.width, 1)
        self.assertEqual(rtg.height, 1)
        self.assertEqual(rtg.x, 1)
        self.assertEqual(rtg.y, 1)
        self.assertEqual(rtg.id, 98)

    def test_new_rect_2(self):
        """Test new rectangle with missing default attrs"""
        rtg = Rectangle(1, 1)
        self.assertEqual(rtg.width, 1)
        self.assertEqual(rtg.height, 1)
        self.assertEqual(rtg.x, 0)
        self.assertEqual(rtg.y, 0)
        self.assertEqual(rtg.id, 1)

    def test_2_rectangles(self):
        """Test 2 new rectangles"""
        rtg = Rectangle(1, 1)
        rtg2 = Rectangle(1, 1)
        self.assertEqual(False, rtg is rtg2)
        self.assertEqual(False, rtg.id == rtg2.id)

    def test_is_Base_instance(self):
        """Test if a rectangle is a Base class instance"""
        rtg = Rectangle(1, 1)
        self.assertEqual(True, isinstance(rtg, Base))

    def test_1_arg(self):
        """Test init method with 1 arg"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1)

    def test_0_arg(self):
        """Test init method with 0 arg"""
        with self.assertRaises(TypeError):
            rtg = Rectangle()

    def test_access_width(self):
        """Trying to access width"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__width

    def test_access_height(self):
        """Trying to access height"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__height

    def test_access_x(self):
        """Trying to access x"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__x

    def test_access_y(self):
        """Trying to access y"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__y

    def test_width_string_attr(self):
        """Test init method with a string attribute as width"""
        with self.assertRaises(TypeError):
            rtg = Rectangle("1", 1)

    def test_height_string_attr(self):
        """Test init method with a string attrubute as height"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1, "1")

    def test_x_string_attr(self):
        """Test init method with a string attribute as x"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1, 1, "1", 1, 1)

    def test_y_string_attr(self):
        """Test init method with a string attribute as y"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1, 1, 1, "1", 1)

    def test_width_0(self):
        """Test init method with a width = 0"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(0, 1)

    def test_height_0(self):
        """"Test init method with a height = 0"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(1, 0)

    def test_x_neg(self):
        """Test init mehtod with negative x"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(1, 1, -1)

    def test_y_neg(self):
        """Test init method with negative y"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(1, 1, 1, -1)
