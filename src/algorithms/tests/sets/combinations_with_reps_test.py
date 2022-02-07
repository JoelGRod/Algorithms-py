import time
import unittest
from algorithms.main.sets.combinations_with_reps import combine_with_reps as cwr


class TestCombinationsWithReps(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f'Time: ({elapsed:.8f}s)')

    def test_combinations_with_reps(self):
        # print("Numbers List", sorted(cwr([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)))
        # print("String", sorted(cwr("123456789", 5)))
        self.assertTrue(sorted(cwr([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)))
        self.assertTrue(sorted(cwr("123456789", 5)))


if __name__ == '__main__':
    unittest.main()
