#!/usr/bin/python3
"""
This module contains the class Base.
"""
import json
import csv
import turtle


class Base:
    """
    Base class for the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of the class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Json representation of a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that saves to a .json file.
        """
        with open(cls.__name__ + ".json", "w", encoding='utf-8') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            list_dic = list()
            for item in list_objs:
                list_dic.append(item.to_dictionary())
            f.write(Base.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """
        Function that returns an object from a json string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Function that returns a new instance from a dictionary.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Function that loads from a json file.
        """
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                elems = cls.from_json_string(f.read())
                ans = []
                for item in elems:
                    ans.append(cls.create(**item))
                return ans
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Function that saves to a .csv file.
        """
        with open(cls.__name__ + ".csv", "w", encoding='utf-8') as f:
            list_dicts = list()
            for item in list_objs:
                list_dicts.append(item.to_dictionary())
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        Function that loads from a .csv file
        """
        ans = []
        with open(cls.__name__ + ".csv", "r") as f:
            reader = csv.DictReader(f)
            for line in reader:
                kwargs = dict(line)
                for key, val in kwargs.items():
                    kwargs[key] = int(val)
                ans.append(cls.create(**kwargs))
            return ans

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Function that draws squares and rectangles.
        """
        my_t = turtle.Turtle()
        for rect in list_rectangles:
            my_t.setheading(0)
            my_t.penup()
            my_t.goto(rect.x, rect.y)
            my_t.pendown()
            my_t.forward(rect.width)
            my_t.right(90)
            my_t.forward(rect.height)
            my_t.right(90)
            my_t.forward(rect.width)
            my_t.right(90)
            my_t.forward(rect.height)
        for squ in list_squares:
            my_t.setheading(0)
            my_t.penup()
            my_t.goto(squ.x, squ.y)
            my_t.pendown()
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
        input()
