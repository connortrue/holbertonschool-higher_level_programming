#!/usr/bin/python3
# 2-matrix_divided.py
# Connor True
"""Doc"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_one_negative_number_in_the_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, -5]), 4)

    def test_only_negative_numbers_in_the_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_list_is_empty(self):
        self.assertEqual(max_integer([]), None)
