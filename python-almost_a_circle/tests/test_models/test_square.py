#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is unit tests for the square case."""

    def test_id_assignment(self):
        """Test for id assignment."""
        square1 = Square(5)
        square2 = Square(2, 1, 3, 12)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square2.id, 12)

    def test_size_assignment(self):
        """Test for size assignment."""
        square1 = Square(5)
        square2 = Square(2, 1, 3, 12)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square2.size, 2)

    def test_x_assignment(self):
        """Test for x assignment."""
        square1 = Square(5)
        square2 = Square(2, 1, 3, 12)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square2.x, 1)

    def test_y_assignment(self):
        """Test for y assignment."""
        square1 = Square(5)
        square2 = Square(2, 1, 3, 12)
        self.assertEqual(square1.y, 0)
        self.assertEqual(square2.y, 3)

    def test_update(self):
        """Test for update method."""
        square1 = Square(5)
        square1.update(89, 2)
        self.assertEqual(square1.id, 89)
        self.assertEqual(square1.size, 2)

    def test_to_dictionary(self):
        """Test for to_dictionary method."""
        square1 = Square(5)
        self.assertEqual(square1.to_dictionary(),
                         {'id': 1, 'size': 5, 'x': 0, 'y': 0})

    def test_size_property(self):
        """Test for size property."""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_update_kwargs(self):
        """Test for update method with keyword arguments."""
        square = Square(5)
        square.update(size=7, id=89)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.id, 89)


if __name__ == '__main__':
    unittest.main()
