import time
import unittest
from algorithms.main.trees.binary_tree_sort_levels import tree_by_levels


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


class TestTreeByLevels(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f'Time: ({elapsed:.8f}s)')

    def test_tree_by_levels(self):
        # Arrange
        self.assertEqual(tree_by_levels(None), [])
        self.assertEqual(tree_by_levels(
            Node(
                Node(
                    None, 
                    Node(
                        None, 
                        None, 
                        4), 
                    2), 
                Node(
                    Node(
                        None, 
                        None, 
                        5), 
                    Node(
                        None, 
                        None, 
                        6), 
                    3), 
                1)), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
