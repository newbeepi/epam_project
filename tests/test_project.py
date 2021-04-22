import pytest


def simple_add(a, b):
    return a+b


def test_simple_add():
    a = 2
    b = 3
    assert simple_add(a, b) == a + b