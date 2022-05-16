import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_1(self):
        actual = fizzbuzz(1)
        expected = 1
        self.assertEqual(actual, expected)
    def test_2(self):
        actual = fizzbuzz(2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_4(self):
        actual = fizzbuzz(4)
        expected = 4
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()