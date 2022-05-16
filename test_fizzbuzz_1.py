import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_10(self):
        actual = fizzbuzz(10)
        expected = 'Buzz'
        self.assertEqual(actual, expected)
    def test_20(self):
        actual = fizzbuzz(20)
        expected = 'Buzz'
        self.assertEqual(actual, expected)

    def test_30(self):
        actual = fizzbuzz(30)
        expected = 'FizzBuzz'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()