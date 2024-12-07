"""
Python Development II Assignment 6: A Fibonacci Series Iterable
Geetha Ramesh

test_fibonacci.py

This module contains unit tests for the Fibonacci class defined in `fibonacci.py`.
The tests verify: input validation for the constructor, behavior of the iterator
for various inputs, handling of negative numbers and raising StopIteration.
"""

import pytest
from fibonacci import Fibonacci


def test_raise_value_error_for_non_integer():
    """
    Test that the Fibonacci constructor raises a ValueError when passed a non-integer.
    """
    with pytest.raises(ValueError):
        Fibonacci("two")
    with pytest.raises(ValueError):
        Fibonacci(6.7)


def test_fibonacci_with_zero():
    """
    Test that Fibonacci(0) produces [0] when cast to a list.
    """
    assert list(Fibonacci(0)) == [0]


def test_fibonacci_with_one():
    """
    Test that Fibonacci(1) produces [0, 1] when cast to a list.
    """
    assert list(Fibonacci(1)) == [0, 1]


def test_fibonacci_with_two():
    """
    Test that Fibonacci(2) produces [0, 1, 1] when cast to a list.
    """
    assert list(Fibonacci(2)) == [0, 1, 1]


def test_fibonacci_with_four():
    """
    Test that Fibonacci(4) produces [0, 1, 1, 2, 3] when cast to a list.
    """
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]


def test_fibonacci_with_ten():
    """
    Test that Fibonacci(10) produces [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] when cast to a list.
    """
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fibonacci_with_negative():
    """
    Test that Fibonacci(-5) produces an empty list when cast to a list.
    """
    assert list(Fibonacci(-5)) == []


def test_fibonacci_stop_iteration():
    """
    Test that Fibonacci raises StopIteration.
    """
    fib = Fibonacci(3)
    iterator = iter(fib)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 1
    assert next(iterator) == 2
    with pytest.raises(StopIteration):
        next(iterator)  # StopIteration should be raised when the sequence ends
