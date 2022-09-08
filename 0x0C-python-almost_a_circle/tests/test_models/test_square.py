#!/usr/bin/python3

"""
Unittest for the class square.
"""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class for testing.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_more_arguments(self):
        """ Test for an instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1, 1, 1)

    def test_correct_inst(self):
        """ Test for a correct instantiation. """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 45)

    def test_str_rep(self):
        """ Test for string representation of a square. """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.__str__(), "[Square] (45) 1/2 - 3")

    def test_size_setter(self):
        """ Test for size setter of square class. """
        s1 = Square(3, 1, 2, 45)
        s1.size = 27
        self.assertEqual(s1.size, 27)

    def test_update(self):
        """ Test for update method of square. """
        s1 = Square(3, 1, 2, 45)
        s1.update(12, 5, 5, 8)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.id, 12)
        s1.update(23)
        self.assertEqual(s1.id, 23)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        s1.update(y=4, x=12, size=8, id=6)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 6)
        s1.update(x=1)
        self.assertEqual(s1.x, 1)
        s1.update(6, x=23)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.x, 1)

    def test_to_dict(self):
        """ Test for to dictionary function. """
        s1 = Square(3, 1, 2, 45)
        s1_d = s1.to_dictionary()
        self.assertDictEqual(s1_d, {'x': 1, 'size': 3, 'id': 45, 'y': 2})

    def test_wrong_size(self):
        """ Test for wrong type for size. """
        with self.assertRaises(TypeError):
            s1 = Square("nope")

    def test_size_zero(self):
        """ Test for a size of zero. """
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_wrong_type_x(self):
        """ Test for a wrong type for x. """
        with self.assertRaises(TypeError):
            s1 = Square(10, "nope")

    def test_wrong_type_y(self):
        """ Test for a wrong type for y. """
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, "nope")

    def test_size_neg(self):
        """ Test for a negative size. """
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_x_neg(self):
        """ Test for a negative x. """
        with self.assertRaises(ValueError):
            s1 = Square(1, -1)

    def test_y_neg(self):
        """ Test for a negative y. """
        with self.assertRaises(ValueError):
            s1 = Square(1, 1, -1)

    def test_to_dict_with_arg(self):
        """ Test calling to_dictionary function with argument. """
        s1 = Square(2)
        with self.assertRaises(TypeError):
            s1.to_dictionary(1)

    def test_create(self):
        """ Test create"""
        s1 = Square.create(**{'id': 89})
        s2 = Square(1, 0, 0, 89)
        self.assertEqual(s1.id, s2.id)

        s3 = Square.create(**{'id': 89, 'size': 1})
        s4 = Square(1, 0, 0, 89)
        self.assertEqual(s3.size, s4.size)

        s5 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        s6 = Square(1, 2, 0, 89)
        self.assertEqual(s5.x, s6.x)

        s7 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        s8 = Square(1, 2, 3, 89)
        self.assertEqual(s8.y, s8.y)

    def test_save_to_file(self):
        """ Test save to file. """
        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))

        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        Square.save_to_file([])
        self.assertTrue(os.path.isfile("Square.json"))

        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.isfile("Square.json"))

    def test_load_from_file(self):
        """ Test load from file"""
        if not os.path.isfile("Square.json"):
            self.assertEqual(Square.load_from_file(), [])
        else:
            objects = Square.load_from_file()
            for obj in objects:
                self.assertIsInstance(obj, Square)
