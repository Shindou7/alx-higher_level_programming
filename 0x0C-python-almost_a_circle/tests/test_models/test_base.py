#!/usr/bin/python3
"""
Unittest for Base Class
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import pep8
import json
import os


class TestPep8(unittest.TestCase):
    def test_pep8_compliance(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Pep8 compliance check failed')


class TestBase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test_given_id(self):
        self.assertEqual(Base(999).id, 999)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(1).id, 1)
        self.assertEqual(Base(-80).id, -80)

    def test_incremented_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_private_attributes(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_created_class(self):
        self.assertEqual(type(Base(100)), Base)

    def test_to_json_string(self):
        dict1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        dict2 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        json_str = Base.to_json_string([dict1, dict2])
        self.assertTrue(type(dict1) == dict)
        self.assertTrue(type(json_str) == str)
        self.assertTrue(json.loads(json_str) == [dict1, dict2])

    def test_to_json_string_with_none(self):
        json_str = Base.to_json_string([None])
        self.assertTrue(type(json_str) == str)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_empty_dict(self):
        empty_dict = dict()
        json_str = Base.to_json_string([empty_dict])
        self.assertTrue(len(empty_dict) == 0)
        self.assertTrue(type(json_str) == str)
        self.assertEqual(json_str, "[]")

    def test_from_json_string(self):
        json_str = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
                    {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        json_list = Base.from_json_string(json_str)
        self.assertTrue(type(json_str) == str)
        self.assertTrue(type(json_list) == list)
        self.assertTrue(type(json_list[0]) == dict)
        self.assertTrue(json_list == [dict1, dict2])
        self.assertTrue(json_list[0] == dict1)

    def test_from_json_string_with_none(self):
        json_list = Base.from_json_string(None)
        self.assertTrue(type(json_list) == list)
        self.assertEqual(json_list, [])

    def test_from_json_string_with_empty_string(self):
        json_list = Base.from_json_string("")
        self.assertTrue(type(json_list) == list)
        self.assertEqual(json_list, [])

    def test_create_instance_from_dictionary(self):
        rectangle_instance = Rectangle(3, 5, 1, 2, 99)
        rect_dict = rectangle_instance.to_dictionary()
        new_rectangle = Rectangle.create(**rect_dict)
        self.assertEqual(str(rectangle_instance), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(new_rectangle), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(rectangle_instance, new_rectangle)

    def test_save_to_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 99)
        rect2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([rect1.to_dictionary(), rect2.to_dictionary()]),
                file.read())

    def test_save_to_file_with_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_file_with_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_file(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 99)
        rectangle2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([rectangle1, rectangle2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        for index, rectangle in enumerate(loaded_rectangles):
            if index == 0:
                self.assertEqual(str(rectangle), '[Rectangle] (99) 2/8 - 10/7')
            if index == 1:
                self.assertEqual(str(rectangle), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_file_with_none(self):
        Rectangle.save_to_file(None)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(type(loaded_rectangles), list)
        self.assertEqual(len(loaded_rectangles), 0)

    def test_load_from_file_with_empty_list(self):
        Rectangle.save_to_file([])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(type(loaded_rectangles), list)
        self.assertEqual(len(loaded_rectangles), 0)
