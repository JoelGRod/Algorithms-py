import unittest
from algorithms.main.misce.directions_reduction import dirReduc

class TestDirectionReduction(unittest.TestCase):
    def test_dir_reduc(self):
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(dirReduc(a), ['WEST'])


if __name__ == '__main__':
    unittest.main()