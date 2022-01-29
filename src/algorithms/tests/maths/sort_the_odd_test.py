import unittest
from algorithms.main.maths.sort_the_odd import sort_array

class TestSortOdds(unittest.TestCase):
    def test_sort_odds(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([]),[])


if __name__ == '__main__':
    unittest.main()
