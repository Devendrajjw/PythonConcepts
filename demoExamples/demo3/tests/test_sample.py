
from demoExamples.demo3.sample import divide
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(1,0)
    assert str(exc_info.value) == "value of  b =0 is not allowed"


def add(a , b):
    return a+b

@pytest.mark.parametrize("a,b,expected",[(2,3,5),(4,5,10)])
def test_add(a,b,expected):
    result = add(a,b)
    assert result==expected
