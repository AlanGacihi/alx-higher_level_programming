#!/usr/bin/python3
"""
Unittest for the class base.
"""
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Class for testing.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_more_arguments(self):
        """ Test for an instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            s1 = Base(1, 1)

    def test_give_id(self):
        """ Creating a Base instance with a specific id. """
        b1 = Base(500)
        self.assertEqual(b1.id, 500)

    def test_to_json_no_args(self):
        """ Test the to_json_string without args. """
        r1 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r1.to_json_string()

    def test_to_json_more_args(self):
        """ Test the to_json_string with more args. """
        r1 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r1.to_json_string([], [])

    def test_to_json_empty(self):
        """ Test the to_json_string with empty list and None. """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.to_json_string([]), "[]")
        self.assertEqual(r1.to_json_string(None), "[]")

    def test_save_to_file_no_args(self):
        """ Test the save_to_file with no arguments. """
        r1 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r1.save_to_file()

    def test_save_to_file_more_args(self):
        """ Test the save_to_file with more arguments. """
        r1 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r1.save_to_file([], [])

    def test_save_to_file_empty(self):
        """ Test the save_to_file with empty list and None. """
        r1 = Rectangle(1, 1)
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        r1.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_save_to_file_csv_empty(self):
        """ Test the save_to_file_csv with empty list and None. """
        r1 = Rectangle(1, 1)
        if os.path.isfile("Rectangle.csv"):
            os.remove("Rectangle.csv")
        r1.save_to_file_csv([])
        self.assertTrue(os.path.isfile("Rectangle.csv"))

    def test_pep8_conformance(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0)
