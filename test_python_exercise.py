from python_exercise import palindrome, freq

def test_palindrome():
    assert palindrome("malayalam")

def test_not_palindrome():
    assert not palindrome("sentence")

def test_null_input_palindrome():
    assert palindrome("")

def test_freq():
    assert {'h': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1} == freq("hello ")
