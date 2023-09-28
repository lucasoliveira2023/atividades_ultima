import pytest

def multi(x, y):
    return x*y

def test_multi():
    assert multi(10, 2) == 20