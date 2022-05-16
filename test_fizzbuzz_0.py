import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_15(self):
        actual = fizzbuzz(15)
        expected = 'FizzBuzz'
        self.assertEqual(actual, expected)
    def test_5(self):
        actual = fizzbuzz(5)
        expected = 'Buzz'
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = fizzbuzz(3)
        expected = 'Fizz'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()