#!/usr/bin/python3
# 2-matrix_divided.py
# Connor True
"""Doc"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer("abc")
