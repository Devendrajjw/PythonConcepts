import pytest
from calculator import Calculator

@pytest.fixture()
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_sub(calc):
    assert calc.sub(3, 1) == 2

@pytest.mark.parametrize('a, b, expected', [(5, 5, 25)])
def test_mul(a, b, expected):
    result = calc.mul(a, b)
    assert result == expected

@pytest.mark.parametrize('a, b, expected', [(25, 5, 5)])
def test_div(a, b, expected):
    result = calc.div(a, b)
    assert result == expected
