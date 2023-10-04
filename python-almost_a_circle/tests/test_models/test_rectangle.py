#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """These are tests for the rectangle class. I don't know how much text you
    really need for a doc but I want at least two lines."""

    def test_setUp(self):
        """Set up for the tests."""
        self.rect1 = Rectangle(5, 4)
        self.rect2 = Rectangle(2, 3, 1, 3, 12)

    def test_id_assignment(self):
        """Test for id assignment."""
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect2.id, 12)

    def test_width_assignment(self):
        """Test for width assignment."""
        self.assertEqual(self.rect1.width, 5)
        self.assertEqual(self.rect2.width, 2)

    def test_height_assignment(self):
        """Test for height assignment."""
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.height, 3)

    def test_x_assignment(self):
        """Test for x assignment."""
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect2.x, 1)

    def test_y_assignment(self):
        """Test for y assignment."""
        self.assertEqual(self.rect1.y, 0)
        self.assertEqual(self.rect2.y, 3)

    def test_area(self):
        """Test for area method."""
        self.assertEqual(self.rect1.area(), 20)
        self.assertEqual(self.rect2.area(), 6)

    def test_update(self):
        """Test for update method."""
        self.rect1.update(89, 2, 3)
        self.assertEqual(self.rect1.id, 89)
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.height, 3)

    def test_to_dictionary(self):
        """Test for to_dictionary method."""
        self.assertEqual(self.rect1.to_dictionary(),
                         {'id': 1, 'width': 5, 'height': 4, 'x': 0, 'y': 0})

    def test_invalid_width(self):
        """Test for invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("invalid", 2)

    def test_invalid_height(self):
        """Test for invalid height."""
        with self.assertRaises(TypeError):
            Rectangle(2, "invalid")

    def test_invalid_x(self):
        """Test for invalid x."""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, "invalid")

    def test_invalid_y(self):
        """Test for invalid y."""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 1, "invalid")


if __name__ == '__main__':
    unittest.main()
