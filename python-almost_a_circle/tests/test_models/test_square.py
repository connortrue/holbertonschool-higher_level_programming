#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_create_square(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square_id(self):
        square = Square(5, id=10)
        self.assertEqual(square.id, 10)

    def test_square_x(self):
        square = Square(5, x=3)
        self.assertEqual(square.x, 3)

    def test_square_y(self):
        square = Square(5, y=4)
        self.assertEqual(square.y, 4)

    def test_square_size_type(self):
        with self.assertRaises(TypeError):
            square = Square("5")

    def test_square_size_value(self):
        with self.assertRaises(ValueError):
            square = Square(-5)

    def test_square_x_type(self):
        with self.assertRaises(TypeError):
            square = Square(5, x="3")

    def test_square_x_value(self):
        with self.assertRaises(ValueError):
            square = Square(5, x=-3)

    def test_square_y_type(self):
        with self.assertRaises(TypeError):
            square = Square(5, y="4")

    def test_square_y_value(self):
        with self.assertRaises(ValueError):
            square = Square(5, y=-4)

    def test_square_str(self):
        square = Square(5, x=1, y=2, id=12)
        self.assertEqual(str(square), "[Square] (12) 1/2 - 5")

    def test_square_update_args(self):
        square = Square(5)
        square.update(12, 7, 2, 3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs(self):
        square = Square(5)
        square.update(id=12, size=7, x=2, y=3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_to_dictionary(self):
        square = Square(5, x=1, y=2, id=12)
        self.assertEqual(square.to_dictionary(), {'id': 12, 'size': 5, 'x': 1, 'y': 2})

    def test_square_size_setter(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_square_size_setter_type(self):
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "10"

    def test_square_size_setter_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -10

    def test_square_update_no_args(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update()

    def test_square_update_extra_args(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(12, 7, 2, 3, 4)

    def test_square_update_extra_kwargs(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(id=12, size=7, x=2, y=3, z=4)

    def test_square_size_zero(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_square_x_zero(self):
        square = Square(5, x=0)
        self.assertEqual(square.x, 0)

    def test_square_y_zero(self):
        square = Square(5, y=0)
        self.assertEqual(square.y, 0)

    def test_square_size_float(self):
        with self.assertRaises(TypeError):
            square = Square(5.5)

    def test_square_x_float(self):
        with self.assertRaises(TypeError):
            square = Square(5, x=3.5)

    def test_square_y_float(self):
        with self.assertRaises(TypeError):
            square = Square(5, y=4.5)

    def test_square_update_args_id_only(self):
        square = Square(5)
        square.update(12)
        self.assertEqual(square.id, 12)

    def test_square_update_args_size_only(self):
        square = Square(5)
        square.update(size=7)
        self.assertEqual(square.size, 7)

    def test_square_update_args_x_only(self):
        square = Square(5)
        square.update(x=2)
        self.assertEqual(square.x, 2)

    def test_square_update_args_y_only(self):
        square = Square(5)
        square.update(y=3)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_id_only(self):
        square = Square(5)
        square.update(id=12)
        self.assertEqual(square.id, 12)

    def test_square_update_kwargs_size_only(self):
        square = Square(5)
        square.update(size=7)
        self.assertEqual(square.size, 7)

    def test_square_update_kwargs_x_only(self):
        square = Square(5)
        square.update(x=2)
        self.assertEqual(square.x, 2)

    def test_square_update_kwargs_y_only(self):
        square = Square(5)
        square.update(y=3)
        self.assertEqual(square.y, 3)

    def test_square_update_args_kwargs(self):
        square = Square(5)
        square.update(12, 7, x=2, y=3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_args(self):
        square = Square(5)
        square.update(id=12, size=7, 2, 3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_no_changes(self):
        square = Square(5)
        square.update()
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_update_kwargs_no_changes(self):
        square = Square(5)
        square.update()
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_size_none(self):
        with self.assertRaises(TypeError):
            square = Square(None)

    def test_square_x_none(self):
        with self.assertRaises(TypeError):
            square = Square(5, x=None)

    def test_square_y_none(self):
        with self.assertRaises(TypeError):
            square = Square(5, y=None)

    def test_square_update_args_none(self):
        square = Square(5)
        square.update(None)
        self.assertEqual(square.id, 1)

    def test_square_update_kwargs_none(self):
        square = Square(5)
        square.update(id=None)
        self.assertEqual(square.id, None)

    def test_square_update_args_size_none(self):
        square = Square(5)
        square.update(size=None)
        self.assertEqual(square.size, 5)

    def test_square_update_kwargs_size_none(self):
        square = Square(5)
        square.update(size=None)
        self.assertEqual(square.size, 5)

    def test_square_update_args_x_none(self):
        square = Square(5)
        square.update(x=None)
        self.assertEqual(square.x, 0)

    def test_square_update_kwargs_x_none(self):
        square = Square(5)
        square.update(x=None)
        self.assertEqual(square.x, 0)

    def test_square_update_args_y_none(self):
        square = Square(5)
        square.update(y=None)
        self.assertEqual(square.y, 0)

    def test_square_update_kwargs_y_none(self):
        square = Square(5)
        square.update(y=None)
        self.assertEqual(square.y, 0)

    def test_square_update_args_id_none(self):
        square = Square(5)
        square.update(None, 7, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_id_none(self):
        square = Square(5)
        square.update(id=None, size=7, x=2, y=3)
        self.assertEqual(square.id, None)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_args_size_none(self):
        square = Square(5)
        square.update(12, None, 2, 3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_size_none(self):
        square = Square(5)
        square.update(id=12, size=None, x=2, y=3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_args_x_none(self):
        square = Square(5)
        square.update(12, 7, None, 3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_x_none(self):
        square = Square(5)
        square.update(id=12, size=7, x=None, y=3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 3)

    def test_square_update_args_y_none(self):
        square = Square(5)
        square.update(12, 7, 2, None)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_square_update_kwargs_y_none(self):
        square = Square(5)
        square.update(id=12, size=7, x=2, y=None)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_square_size_negative(self):
        with self.assertRaises(ValueError):
            square = Square(-5)

    def test_square_x_negative(self):
        with self.assertRaises(ValueError):
            square = Square(5, x=-1)

    def test_square_y_negative(self):
        with self.assertRaises(ValueError):
            square = Square(5, y=-1)

    def test_square_update_args_negative(self):
        square = Square(5)
        square.update(-89, 2)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)

    def test_square_update_kwargs_negative(self):
        square = Square(5)
        square.update(id=-89)
        self.assertEqual(square.id, 1)

    def test_square_update_args_size_negative(self):
        square = Square(5)
        square.update(89, -2)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 5)

    def test_square_update_kwargs_size_negative(self):
        square = Square(5)
        square.update(size=-7)
        self.assertEqual(square.size, 5)

    def test_square_update_args_x_negative(self):
        square = Square(5)
        square.update(89, 2, -3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 0)

    def test_square_update_kwargs_x_negative(self):
        square = Square(5)
        square.update(x=-2)
        self.assertEqual(square.x, 0)

    def test_square_update_args_y_negative(self):
        square = Square(5)
        square.update(89, 2, 3, -4)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 0)

    def test_square_update_kwargs_y_negative(self):
        square = Square(5)
        square.update(y=-3)
        self.assertEqual(square.y, 0)

    def test_square_update_args_id_negative(self):
        square = Square(5)
        square.update(-89, 7, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_id_negative(self):
        square = Square(5)
        square.update(id=-89, size=7, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_args_size_negative(self):
        square = Square(5)
        square.update(12, -7, 2, 3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_size_negative(self):
        square = Square(5)
        square.update(id=12, size=-7, x=2, y=3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_args_x_negative(self):
        square = Square(5)
        square.update(12, 7, -2, 3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 3)

    def test_square_update_kwargs_x_negative(self):
        square = Square(5)
        square.update(id=12, size=7, x=-2, y=3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 3)

    def test_square_update_args_y_negative(self):
        square = Square(5)
        square.update(12, 7, 2, -3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_square_update_kwargs_y_negative(self):
        square = Square(5)
        square.update(id=12, size=7, x=2, y=-3)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

if __name__ == '__main__':
    unittest.main()