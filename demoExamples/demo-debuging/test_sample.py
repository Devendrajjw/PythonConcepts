import pytest

def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    assert result == 6  # This will fail


def test_example():
    x = 1
    y = 2
    pytest.set_trace()  # Start debugger here
    assert x + y == 3
