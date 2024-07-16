# test_example.py

from pytest_bdd import scenarios, given, when, then

# Load the feature file
scenarios('example.feature')

# Define the steps
@given('I have two numbers 2 and 3', target_fixture="numbers")
def numbers():
    return 2, 3

@when('I add them',target_fixture="add")
def add(numbers):
    a, b = numbers
    return a + b

@then('the result should be 5')
def result(add):
    assert add == 5
