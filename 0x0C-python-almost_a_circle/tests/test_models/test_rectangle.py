#!/usr/bin/python3
"""
Unittest for the class Rectangle.
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Class for testing.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_more_arguments(self):
        """ Test for an instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)

    def test_less_arguments(self):
        """ Test for less arguments than required. """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_correct_inst(self):
        """ Test for a correct instantiation. """
        r1 = Rectangle(3, 5, 1, 2, 45)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 45)
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_wrong_type_width(self):
        """ Test for a wrong type for width. """
        with self.assertRaises(TypeError):
            r1 = Rectangle("nope", 5)

    def test_wrong_type_height(self):
        """ Test for a wrong type for height. """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, "nope")

    def test_wrong_type_x(self):
        """ Test for a wrong type for x. """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, "nope")

    def test_wrong_type_y(self):
        """ Test for a wrong type for y. """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, 1, "nope")

    def test_width_zero(self):
        """ Test for a width of 0. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 5)

    def test_height_zero(self):
        """ Test for a height of 0. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    def test_width_neg(self):
        """ Test for a negative width. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 5)

    def test_height_neg(self):
        """ Test for a negative height. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, -1)

    def test_x_neg(self):
        """ Test for a negative x. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 5, -1)

    def test_y_neg(self):
        """ Test for a negative y. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 5, 1, -1)

    def test_setters_ok(self):
        """ Test for setters with good values. """
        r1 = Rectangle(1, 5)
        r1.width = 2
        r1.height = 6
        r1.x = 3
        r1.y = 4
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_width_setter_wrong(self):
        """ Test for wrong type for width setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r1.width = "nope"

    def test_height_setter_wrong(self):
        """ Test for wrong type for height setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r1.height = "nope"

    def test_x_setter_wrong(self):
        """ Test for wrong type for x setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r1.x = "nope"

    def test_y_setter_wrong(self):
        """ Test for wrong type for y setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r1.y = "nope"

    def test_width_setter_zero(self):
        """ Test with 0 for width setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r1.width = 0

    def test_height_setter_zero(self):
        """ Test with 0 for height setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r1.height = 0

    def test_width_setter_negative(self):
        """ Test with negative for width setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r1.width = -1

    def test_height_setter_negative(self):
        """ Test with negative for height setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r1.height = -1

    def test_x_setter_negative(self):
        """ Test with negative for x setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r1.x = -1

    def test_y_setter_negative(self):
        """ Test with negative for y setter. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            r1.y = -1

    def test_area_with_arg(self):
        """ Test calling area function with argument. """
        r1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r1.area(1)

    def test_area_ok(self):
        """ Test the area function. """
        r1 = Rectangle(5, 7)
        r2 = Rectangle(1, 2)
        r3 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 35)
        self.assertEqual(r2.area(), 2)
        self.assertEqual(r3.area(), 50)

    def test_display_with_arg(self):
        """ Test calling display function with argument. """
        r1 = Rectangle(2, 1)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_display_ok(self):
        """ Test the display function. """
        r1 = Rectangle(2, 3, 1, 1)
        outr1 = StringIO()
        with redirect_stdout(outr1):
            r1.display()
            self.assertEqual(outr1.getvalue(), "\n ##\n ##\n ##\n")

    def test_str_rep(self):
        """ Test for string representation of a rectangle. """
        r1 = Rectangle(3, 5, 1, 2, 45)
        self.assertEqual(r1.__str__(), "[Rectangle] (45) 1/2 - 3/5")

    def test_update(self):
        """ Test for update method of rectangle. """
        r1 = Rectangle(3, 5, 1, 2, 45)
        r1.update(12, 9, 5, 5, 8)
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 12)
        r1.update(23)
        self.assertEqual(r1.id, 23)
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 8)
        r1.update(y=4, x=12, width=8, id=6, height=99)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 99)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 6)
        r1.update(x=1)
        self.assertEqual(r1.x, 1)
        r1.update(6, x=23)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.x, 1)

    def test_to_dict(self):
        """ Test for to dictionary function. """
        r1 = Rectangle(3, 5, 1, 2, 45)
        r1_d = r1.to_dictionary()
        dic = {'x': 1, 'width': 3, 'id': 45, 'y': 2, 'height': 5}
        self.assertDictEqual(r1_d, dic)

    def test_to_dict_with_arg(self):
        """ Test calling to_dictonary function with argument. """
        r1 = Rectangle(2, 1)
        with self.assertRaises(TypeError):
            r1.to_dictionary(1)
