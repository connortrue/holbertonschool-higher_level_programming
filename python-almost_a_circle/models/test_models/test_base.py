import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_with_no_argument(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_with_argument(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_id_with_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
