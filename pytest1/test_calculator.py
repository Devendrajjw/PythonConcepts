import pytest
from calculator import Calculator
import logging

@pytest.fixture
def calc():
    logging.log()
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_sub(calc):
    assert calc.sub(3, 1) == 2
