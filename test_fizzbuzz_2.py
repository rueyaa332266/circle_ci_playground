import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_22(self):
        actual = fizzbuzz(22)
        expected = 22
        self.assertEqual(actual, expected)
    def test_33(self):
        actual = fizzbuzz(33)
        expected = 'Fizz'
        self.assertEqual(actual, expected)

    def test_44(self):
        actual = fizzbuzz(44)
        expected = 44
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()