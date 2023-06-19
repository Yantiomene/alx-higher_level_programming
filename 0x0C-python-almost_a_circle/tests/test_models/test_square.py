#!/usr/bin/python3
"""Class test cases for square methods"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestSquareMethods(unittest.TestCase):
    """Test suite for Square class methods"""

    def setUp(self):
        """setUp method"""
        Base._Base__nb_objects = 0

    def test_square_1_arg(self):
        """Test init method with 1 arg"""
        s = Square(2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square_args(self):
        """Test init method with all args"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_squares(self):
        """Test 2 squares"""
        s = Square(1)
        s2 = Square(1)
        self.assertEqual(False, s is s2)
        self.assertEqual(False, s.id == s2.id)

    def test_is_Rect_instance(self):
        """Test square is a Rectangle instance"""
        s = Square(1)
        self.assertEqual(True, isinstance(s, Rectangle))

    def test_is_Base_instance(self):
        """Test square is a Base instance"""
        s = Square(1)
        self.assertEqual(True, isinstance(s, Base))

    def test_0_arg(self):
        """Test with 0 args"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_5_args(self):
        """Test with 5 args"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_access_width(self):
        """Test accessing width"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__width

    def test_access_height(self):
        """Test accessing height"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__height

    def test_access_x(self):
        """Test accessing x"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__x

    def test_access_y(self):
        """Test accessing y"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__y

    def test_valid_size(self):
        """Test size string"""
        with self.assertRaises(TypeError):
            s = Square("1", 1, 2, 2)

    def test_valid_x(self):
        """Test x string"""
        with self.assertRaises(TypeError):
            s = Square(1, '1', 1, 1)

    def test_valid_y(self):
        """Test y string"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, '1', 1)

    def test_size_0(self):
        """Test case of a size 0"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_x_neg(self):
        """Test case for x negative"""
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_y_neg(self):
        """Test case for y negative"""
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def test_area(self):
        """Test the return value of the area method"""
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_area_size(self):
        """Test area and update size"""
        s = Square(3)
        self.assertEqual(s.area(), 9)
        s.size = 5
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test printed string"""
        s = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_display_size(self):
        """Test printed string and modified size"""
        s = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

        s.size = 3
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_dislay_xy(self):
        """Test string printed with x and y"""
        s = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

        s.x = 1
        res = " ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

        s.y = 2
        res = "\n\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_str(self):
        """Test the __str___ return value"""
        s = Square(2)
        res = "[Square] (1) 0/0 - 2"
        self.assertEqual(s.__str__(), res)

    def test_str_2(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_str_3(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2, 2)
        res = "[Square] (2) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s.id = 1
        s.size = 10
        res = "[Square] (1) 2/2 - 10\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_str_4(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s2 = Square(2)
        res = "[Square] (2) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s2)
            self.assertEqual(std_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s3)
            self.assertEqual(std_out.getvalue(), res)
