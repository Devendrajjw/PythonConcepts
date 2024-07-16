import pytest
from . import Calculator


@pytest.fixture()
def calc():
    return Calculator()

def test_add(calc):
    assert calc.addcal(2, 3) == 5

def test_sub(calc):
    assert calc.subcal(3, 1) == 2
