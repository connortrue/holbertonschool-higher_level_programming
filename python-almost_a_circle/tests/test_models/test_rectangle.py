#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import unittest
from models.rectangle import Rectangle
import json


class TestRectangle(unittest.TestCase):
    """These are unit tests for the Rectangle class."""

    def test_id_assignment(self):
        """Test for id assignment."""
        rect1 = Rectangle(5, 4)
        rect2 = Rectangle(2, 3, 1, 1, 12)
        rect3 = Rectangle(7, 8)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 12)
        self.assertEqual(rect3.id, 2)

    def test_area(self):
        """Test for area method."""
        rect1 = Rectangle(5, 4)
        rect2 = Rectangle(2, 3)
        self.assertEqual(rect1.area(), 20)
        self.assertEqual(rect2.area(), 6)

    def test_to_dictionary(self):
        """Test for to_dictionary method."""
        rect1 = Rectangle(5, 4)
        self.assertEqual(rect1.to_dictionary(),
                         {'id': 1, 'width': 5, 'height': 4, 'x': 0, 'y': 0})

    def test_update(self):
        """Test for update method."""
        rect1 = Rectangle(5, 4)
        rect1.update(89, 2, 3)
        self.assertEqual(rect1.id, 89)
        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect1.height, 3)

    def test_save_to_file(self):
        """Test for save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps([r1.to_dictionary(),
                                        r2.to_dictionary()]), file.read())

    def test_load_from_file(self):
        """Test for load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        load_rectangles = Rectangle.load_from_file()
        self.assertEqual(r1.__dict__, load_rectangles[0].__dict__)
        self.assertEqual(r2.__dict__, load_rectangles[1].__dict__)


if __name__ == '__main__':
    unittest.main()
