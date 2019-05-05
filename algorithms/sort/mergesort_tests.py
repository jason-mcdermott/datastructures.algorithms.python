import unittest
import mergesort

numbers = [3, 5, 2, 9, 10, 8, 1, 4, 6, 7 ]
sorted = mergesort.sort([3, 5, 2, 9, 10, 8, 1, 4, 6, 7 ])

class IterativeSearchTests(unittest.TestCase):
    """Tests for the iterative.binary_search() function"""

    def test_1(self):
        """sorted list should have 1 at index 0"""
        self.assertEqual(sorted[0], 1)

    def test_2(self):
        """sorted list should have 2 at index 1"""
        self.assertEqual(sorted[1], 2)

    def test_3(self):
        """sorted list have 5 at index 4"""
        self.assertEqual(sorted[4], 5)

    def test_4(self):
        """sorted list have 10 at index 9"""
        self.assertEqual(sorted[9], 10)

if __name__ == '__main__':
    unittest.main()