import unittest
from python_exercise import palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        sentence = "malayalam"
        self.assertTrue(palindrome(sentence))

if __name__ == "__main__":
    unittest.main()
