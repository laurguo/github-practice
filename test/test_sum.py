import pytest 

def sum(a, b):
    return a + b

def test_sum():
    assert sum(2, -13) == -11