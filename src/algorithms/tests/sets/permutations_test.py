import time
import unittest
from algorithms.main.sets.permutations import permutations_no_rep as pnr, permutations_no_rep_two as pnrtwo, permutations_no_rep_three as pnrthree


class TestPermutations(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f'Time: ({elapsed:.8f}s)')

    def test_permutations_no_rep(self):
        self.assertEqual(sorted(pnr('a')), ['a'])
        self.assertEqual(sorted(pnr('ab')), ['ab', 'ba'])
        self.assertTrue(sorted(pnr('MISSISSIPPI')))
        self.assertEqual(sorted(pnr('aabb')), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
        self.assertEqual(sorted(pnr(['a'])), ['a'])
        self.assertEqual(sorted(pnr(['a','b'])), ['ab', 'ba'])
        self.assertEqual(sorted(pnr(['a','a','b','b'])), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

    def test_permutations_no_rep_two(self):
        self.assertEqual(sorted(pnrtwo('a')), ['a'])
        self.assertEqual(sorted(pnrtwo('ab')), ['ab', 'ba'])
        self.assertTrue(sorted(pnr('MISSISSIPPI')))
        self.assertEqual(sorted(pnrtwo('aabb')), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
        self.assertEqual(sorted(pnrtwo(['a'])), ['a'])
        self.assertEqual(sorted(pnrtwo(['a','b'])), ['ab', 'ba'])
        self.assertEqual(sorted(pnrtwo(['a','a','b','b'])), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
                         
    def test_permutations_no_rep_three(self):
        self.assertEqual(sorted(pnrthree('a')), ['a'])
        self.assertEqual(sorted(pnrthree('ab')), ['ab', 'ba'])
        self.assertTrue(sorted(pnr('MISSISSIPPI')))
        self.assertEqual(sorted(pnrthree('aabb')), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
        self.assertEqual(sorted(pnrthree(['a'])), ['a'])
        self.assertEqual(sorted(pnrthree(['a','b'])), ['ab', 'ba'])
        self.assertEqual(sorted(pnrthree(['a','a','b','b'])), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
