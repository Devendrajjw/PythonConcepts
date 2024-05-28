# -- FILE: bdd/features/steps.py
from behave import given, when, then


@given('I have entered {x:d} into the calculator')
def step_enter_number(context, x):
    context.number = x


@when('I press add')
def step_press_add(context):
    context.result = context.number + context.number2


@then('the result should be {expected_result: d} on the screen')
def step_check_result(context, expected_result):
    assert context.result == expected_result, f'Expected {expected_result}, but got {context.result}'
