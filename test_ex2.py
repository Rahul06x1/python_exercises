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
    assert not evaluate('23a')

def test_symbol():
    assert not evaluate('21@')

def test_null():
    assert not evaluate('')

def test_single_value():
    assert evaluate('1+') == 1 