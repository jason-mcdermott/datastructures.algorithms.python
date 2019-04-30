import unittest
import iterative

numbers = [1,2,3,4,5,6,7,8,9,10]

class IterativeSearchTests(unittest.TestCase):
    """Tests for the iterative.binary_search() function"""

    def test_1(self):
        """should return True when the target is 4"""
        self.assertEqual(iterative.binary_search(numbers, 4), True)

    def test_2(self):
        """should return True when the target is 10"""
        self.assertEqual(iterative.binary_search(numbers, 10), True)

    def test_3(self):
        """should return False when the target is 0"""
        self.assertEqual(iterative.binary_search(numbers, 0), False)

    def test_4(self):
        """should return False when the target is 12"""
        self.assertEqual(iterative.binary_search(numbers, 12), False)

if __name__ == '__main__':
    unittest.main()