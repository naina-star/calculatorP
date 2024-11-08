import pytest
from calculator import Calculator

def test_add():
    # Test addition with precision of 5 decimal places.
    calc = Calculator(precision=5)
    assert calc.add(2, 3) == 5.0

def test_subtract():
    # Test subtraction with precision of 5 decimal places.
    calc = Calculator(precision=5)
    assert calc.subtract(5, 3) == 2.0

def test_multiply():
    # Test multiplication with precision of 5 decimal places.
    calc = Calculator(precision=5)
    assert calc.multiply(2, 3) == 6.0

def test_divide():
    # Test division with precision of 5 decimal places.
    calc = Calculator(precision=5)
    assert calc.divide(6, 3) == 2.0

def test_divide_by_zero():
    # Ensure dividing by zero raises the appropriate error.
    calc = Calculator(precision=5)
    with pytest.raises(ValueError):
        calc.divide(2, 0)

def test_power():
    # Test power operation with precision of 5 decimal places.
    calc = Calculator(precision=5)
    assert calc.power(2, 3) == 8.0

def test_root():
    # Test square root operation with precision of 5 decimal places.
    calc = Calculator(precision=5)
    assert calc.root(8, 3) == 2.0
