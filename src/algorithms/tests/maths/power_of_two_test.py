import unittest
from algorithms.main.maths.power_of_two import (
    power_of_two as pot, 
    power_of_two_naive as potn
)

class PowerOfTwo(unittest.TestCase):
	def test_power_of_two_naive(self):
		self.assertEqual(potn(0), False)
		self.assertEqual(potn(1), True)
		self.assertEqual(potn(2), True)
		self.assertEqual(potn(3), False)
		self.assertEqual(potn(4), True)
		self.assertEqual(potn(8), True)
		self.assertEqual(potn(16), True)
		self.assertEqual(potn(1024), True)
		self.assertEqual(potn(1025), False)

	def test_power_of_two(self):
		self.assertEqual(pot(0), False)
		self.assertEqual(pot(1), True)
		self.assertEqual(pot(2), True)
		self.assertEqual(pot(3), False)
		self.assertEqual(pot(4), True)
		self.assertEqual(pot(8), True)
		self.assertEqual(pot(16), True)
		self.assertEqual(pot(1024), True)
		self.assertEqual(pot(1025), False)

if __name__ == '__main__':
    unittest.main()