#!/usr/bin/python3
"""
Module contains class Base
Write the first class Base:
Create a folder named models with an empty file __init__.py inside
with this file, the folder will become a Python package
Create a file named models/base.py:
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)
"""


import json
import csv
from os import path
import turtle


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """List to JSON strin"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string representation """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            list_dic = []

            for elem in list_objs:
                list_dic.append(elem.to_dictionary())

            return f.write(cls.to_json_string(list_dic))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            list_objs = cls.from_json_string(f.read())
            list_dic = []

            for elem in list_objs:
                list_dic.append(cls.create(**elem))

            return list_dic

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"

        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if 'width' in row and 'height' in row:
                    dic = {
                        "id": int(row['id']),
                        "width": int(row['width']),
                        "height": int(row['height']),
                        "x": int(row['x']),
                        "y": int(row['y'])
                    }
                    o = cls.create(**dic)
                    objs.append(o)
                elif 'size' in row:
                    dic = {
                        "id": int(row['id']),
                        "size": int(row['size']),
                        "x": int(row['x']),
                        "y": int(row['y'])
                    }
                    o = cls.create(**dic)
                    objs.append(o)

        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        def draw_shape(shape, color):
            turt.showturtle()
            turt.up()
            turt.goto(shape.x, shape.y)
            turt.down()
            turt.color(color)
            for i in range(2):
                turt.forward(shape.width)
                turt.left(90)
                turt.forward(shape.height)
                turt.left(90)
            turt.hideturtle()
        for rect in list_rectangles:
            draw_shape(rect, "#ffffff")
        for sq in list_squares:
            draw_shape(sq, "#b5e3d8")

        turtle.exitonclick()
