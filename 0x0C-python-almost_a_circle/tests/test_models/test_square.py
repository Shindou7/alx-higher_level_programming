#!/usr/bin/python3
"""
Unittest for Square Class
"""


import unittest
import pep8
from io import StringIO
from contextlib import redirect_stdout
from models import square as s
Square = s.Square

class TestPep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=False)
        errors = style.check_files(["models/square.py", "tests/test_models/test_square.py"]).total_errors
        self.assertEqual(errors, 0, 'Pep8 compliance check failed')

class TestSquare(unittest.TestCase):
    def test_attributes(self):
        square1 = Square(9, 99, 999, 1000)
        self.assertEqual(square1.width, 9)
        self.assertEqual(square1.height, 9)
        self.assertEqual(square1.size, 9)
        self.assertEqual(square1.x, 99)
        self.assertEqual(square1.y, 999)
        self.assertEqual(square1.id, 1000)

    def test_default_attributes(self):
        square2 = Square(88)
        self.assertEqual(square2.width, 88)
        self.assertEqual(square2.height, 88)
        self.assertEqual(square2.size, 88)
        self.assertEqual(square2.x, 0)
        self.assertEqual(square2.y, 0)
        self.assertIsNotNone(square2.id)

    def test_attribute_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, 3])
            Square({20, })
            Square({"d": 20})
            Square(None)
            Square((30, 20), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_class_creation(self):
        self.assertEqual(type(Square(10)), Square)

    def test_area_method(self):
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display_method(self):
        with StringIO() as buf, redirect_stdout(buf):
            Square(4).display()
            b = buf.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as buf, redirect_stdout(buf):
            Square(3, 1, 2).display()
            b = buf.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_string_representation(self):
        square = Square(1, 2, 3, 44)
        square.size = 500
        self.assertEqual(str(square), '[Square] (44) 2/3 - 500')

    def test_update_method(self):
        square = Square(1, 2, 3, 4)
        square.update(10, 10, 10, 10)
        self.assertEqual(str(square), '[Square] (10) 10/10 - 10')
        square.update()
        self.assertEqual(str(square), '[Square] (10) 10/10 - 10')
        square.update(99)
        self.assertEqual(str(square), '[Square] (99) 10/10 - 10')
        square.update(99, 5)
        self.assertEqual(str(square), '[Square] (99) 10/10 - 5')
        square.update(44, 55, 1, 2)
        self.assertEqual(str(square), '[Square] (44) 1/2 - 55')
        square.update(id=88, size=77, nokey=99)
        self.assertEqual(str(square), '[Square] (88) 1/2 - 77')

    def test_to_dictionary_method(self):
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        square2 = Square(10, 10)
        square2.update(**sdic)
        self.assertEqual(str(square2), '[Square] (4) 2/3 - 1')

if __name__ == '__main__':
    unittest.main()
