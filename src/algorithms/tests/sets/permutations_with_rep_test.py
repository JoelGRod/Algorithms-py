import time
import unittest
from algorithms.main.sets.permutations_with_rep import permutations as pwr


class TestPermutationsWithReps(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f'Time: ({elapsed:.8f}s)')

    def test_permutations_with_rep(self):
        # print(pwr('1234', 6))
        # print(pwr([1,2,3,4], 2))
        # print(pwr(["1","2","3","4"], 2))
        self.assertTrue(sorted(pwr('1234')))
        self.assertTrue(sorted(pwr([1, 2, 3, 4])))
        self.assertTrue(sorted(pwr(["1", "2", "3", "4"])))


if __name__ == '__main__':
    unittest.main()
