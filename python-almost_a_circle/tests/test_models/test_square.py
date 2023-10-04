#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is unit tests for the square case. I don't know how much more
    documentation you require. Beep Boop."""

    def test_setUp(self):
        """Set up for the tests."""
        self.square1 = Square(5)
        self.square2 = Square(2, 1, 3, 12)

    def test_id_assignment(self):
        """Test for id assignment."""
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(self.square2.id, 12)

    def test_size_assignment(self):
        """Test for size assignment."""
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square2.size, 2)

    def test_x_assignment(self):
        """Test for x assignment."""
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square2.x, 1)

    def test_y_assignment(self):
        """Test for y assignment."""
        self.assertEqual(self.square1.y, 0)
        self.assertEqual(self.square2.y, 3)

    def test_update(self):
        """Test for update method."""
        self.square1.update(89, 2)
        self.assertEqual(self.square1.id, 89)
        self.assertEqual(self.square1.size, 2)

    def test_to_dictionary(self):
        """Test for to_dictionary method."""
        self.assertEqual(self.square1.to_dictionary(),
                         {'id': 1, 'size': 5, 'x': 0, 'y': 0})


if __name__ == '__main__':
    unittest.main()
