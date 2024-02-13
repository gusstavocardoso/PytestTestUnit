import pytest
from src.math_operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_multiply_negative_numbers():
    assert multiply(-3, 2) == -6
    assert multiply(3, -2) == -6
    assert multiply(-3, -2) == 6

def test_add_large_numbers():
    assert add(10**20, 10**20) == 2 * 10**20

def test_subtract_negative_numbers():
    assert subtract(5, 8) == -3
    assert subtract(-5, -8) == 3
    assert subtract(-5, 8) == -13

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(-5, 0) == -5

def test_subtract_zero():
    assert subtract(5, 0) == 5
    assert subtract(-5, 0) == -5
    assert subtract(0, 0) == 0

def test_multiply_zero():
    assert multiply(5, 0) == 0
    assert multiply(-5, 0) == 0
    assert multiply(0, 0) == 0

def test_divide_one():
    assert divide(5, 1) == 5
    assert divide(-5, 1) == -5
    assert divide(0, 1) == 0
