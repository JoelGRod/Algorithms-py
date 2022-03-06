import time
import unittest
from algorithms.main.sets.two_sum_target import two_sum


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f'Time: ({elapsed:.8f}s)')

    def test_two_sum(self):
        # Arrange
        input = [9, 4, 20, 3, 39, 12, 1, 4, 6]
        # Act
        # Assert
        self.assertEqual(two_sum(input, 45), [4, 8])


if __name__ == '__main__':
    unittest.main()