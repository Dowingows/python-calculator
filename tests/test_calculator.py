import pytest
from calculator.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0
    assert multiply(-1, 1) == -1
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError):
        divide(4, 0)