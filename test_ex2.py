from ex2 import evaluate

def test_evaluate():
    assert  evaluate("6")== 6

def test_add():
    assert evaluate("23+") == 5

def test_sub():
    assert evaluate("32-") == 1

def test_div():
    assert evaluate("62/") == 3

def test_mul():
    assert evaluate('23*') == 6

def test_alphabet():
    assert evaluate('23a') == False

def test_symbol():
    assert evaluate('21@') == False

def test_null():
    assert evaluate('') == False