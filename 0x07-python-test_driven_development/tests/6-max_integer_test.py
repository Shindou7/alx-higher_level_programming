#!/usr/bin/python3
"""Unittest max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestMaxIntege max_integer function"""

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_positive_and_negative_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.7, 3.3, 4.1])
        self.assertEqual(result, 4.1)

    def test_mixed_integer_and_float_numbers(self):
        result = max_integer([1, 2.5, 3, 4.9])
        self.assertEqual(result, 4.9)

    def test_duplicate_max_value(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_list_with_None(self):
        result = max_integer([None, 1, 2])
        self.assertEqual(result, 2)

    def test_list_with_strings(self):
        with self.assertRaises(TypeError):
            max_integer(["apple", "banana", "cherry"])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, "four"])


if __name__ == "__main__":
    unittest.main()
