
from demoExamples.demo.sample import func
from demoExamples.demo.sample import add
import pytest

def test_answer():
    assert func(3) == 5

@pytest.mark.sanity
@pytest.mark.slow
def test_answer1():
    assert func(4) == 5


# Test function using 4A pattern

@pytest.mark.slow
def test_add():
    # Arrange: Set up the conditions for the test
    a = 2
    b = 3
    expected_result = 6

    # Act: Perform the action that you want to test
    result = add(a, b)

    # Assert: Verify that the outcome of the action matches your expectations
    assert result == expected_result

    # Cleanup: (Not needed in this simple example, but this is where you would clean up any resources or state changes)


@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(5)
    assert True

