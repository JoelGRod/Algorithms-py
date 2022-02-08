import unittest
from algorithms.main.misce.ranking_system import User


class TestRankingSystem(unittest.TestCase):
    user = User()

    def test_ranking_system(self):
        self.assertEqual(self.user.rank, -8)
        self.assertEqual(self.user.progress, 0)
        self.user.inc_progress(-7)
        self.assertEqual(self.user.progress, 10)
        self.user.inc_progress(-5)
        self.assertEqual(self.user.progress, 0)
        self.assertEqual(self.user.rank, -7)


if __name__ == '__main__':
    unittest.main()