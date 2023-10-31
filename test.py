import unittest
from python_exercise import palindrome, freq

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        sentence = "malayalam"
        self.assertTrue(palindrome(sentence))

    def test_not_palindrome(self):
        sentence = "sentence"
        self.assertFalse(palindrome(sentence))
    
    def test_null_input(self):
        self.assertTrue(palindrome(""))


class TestFreq(unittest.TestCase):

    def test_freq(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        d = {'t': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 
             'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 
             'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 
             'y': 1, 'd': 1, 'g': 1}
        self.assertDictEqual(d, freq(sentence))

if __name__ == "__main__":
    unittest.main()
