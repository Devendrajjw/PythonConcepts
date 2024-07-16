import pytest
# test_example.py
import math

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 3 # This will fail

def test_multiplication():
    assert 2 * 2 == 5  # This will fail

def test_division():
    assert 10 / 2 == 5

def test_square_root():
    assert math.sqrt(16) == 5  # This will fail
