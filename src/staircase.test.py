import unittest
from staircase import ways_up


class StaircaseTestCase(unittest.TestCase):
    def test_base_case(self):
        steps = ways_up(1, [1, 2])
        self.assertEqual(steps, 1)

    def test_base_3(self):
        steps = ways_up(3, [1, 2])
        self.assertEqual(steps, 3)

    def test_base_5(self):
        steps = ways_up(5, [1, 2])
        self.assertEqual(steps, 8)

    def test_advanced_5(self):
        steps = ways_up(5, [1, 3, 5])
        self.assertEqual(steps, 5)

    def test_advanced_8(self):
        steps = ways_up(8, [1, 3, 5])
        self.assertEqual(19, steps)


if __name__ == '__main__':
    unittest.main()
