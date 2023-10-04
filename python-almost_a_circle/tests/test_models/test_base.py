#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """These are unit tests for the base class. Not sure how much
    documentation is required so I'll stop here."""

    def test_setUp(self):
        """Set up for the tests."""
        self.base1 = Base()
        self.base2 = Base(12)
        self.base3 = Base()

    def test_id_assignment(self):
        """Test for id assignment."""
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 12)
        self.assertEqual(self.base3.id, 2)

    def test_to_json_string(self):
        """Test for to_json_string method."""
        list_dict = [{'id': 12}, {'id': 13}]
        self.assertEqual(Base.to_json_string(list_dict),
                         '[{"id": 12}, {"id": 13}]')

    def test_from_json_string(self):
        """Test for from_json_string method."""
        list_str = '[{"id": 12}, {"id": 13}]'
        self.assertEqual(Base.from_json_string(list_str), [{'id': 12},
                                                           {'id': 13}])

    def test_create(self):
        """Test for create method."""
        base_dict = {'id': 42}
        base = Base.create(**base_dict)
        self.assertEqual(base.id, 42)

    def test_save_to_file(self):
        """Test for save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps([r1.to_dictionary(), r2.to_dictionary()]), file.read())

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
