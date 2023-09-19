#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""


from models.rectangle import Rectangle
from models.base import Base
from unittest import mock
import unittest
import pep8
import io


class TestPep8(unittest.TestCase):
    def test_pep8_compliance(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Pep8 compliance check failed')


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 99)

    def test_default_attributes(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertIsNotNone(r2.id)

    def test_attribute_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 1, 1, 1, 1)
            Rectangle([10, 3], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"d": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -20, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -99, 1)

    def test_private_attributes_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_class_creation(self):
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    def test_area_method(self):
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_method(self):
        r = Rectangle(2, 3, 1, 1, 99)
        expected_output = "\n ##\n ##\n ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_string_representation(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update_method(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')

    def test_to_dictionary_method(self):
        rdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**rdic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')
