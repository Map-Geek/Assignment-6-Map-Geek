"""
Python Development II Assignment 6: A Fibonacci Series Iterable
Geetha Ramesh

fibonacci.py

This module defines the Fibonacci class, which provides an iterable for generating
Fibonacci sequences.
"""


class Fibonacci:
    """
    An iterable class to generate the Fibonacci sequence.

    Attributes:
        num (int): The number of Fibonacci terms to generate.

    Methods:
    __iter__(): Returns the iterator object (self).
    __next__(): Produces the next Fibonacci number in the sequence.
    """

    def __init__(self, num):
        """
        Initializes the Fibonacci iterator with the specified number of terms.
        :param num: number of terms to generate in the Fibonacci sequence
        :raises Value Error: If number is not an integer.
        """
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")
