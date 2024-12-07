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
        num: The number of Fibonacci terms to generate.
        count: Tracks the current position in the sequence during iteration.
        current_num: Holds the current Fibonacci number in the sequence.
        next_num: Holds the next Fibonacci number in the sequence.

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

        if num < 0:
            self.num = 0  # If negative input, default to 0
        else:
            self.num = num
        self.count = 0
        self.current_num, self.next_num = 0, 1  # Initialize the first two Fibonacci numbers

    def __iter__(self):
        """
        Returns: Fibonacci: The iterator object itself.
        """
        return self  # The instance itself acts as the iterator

    def __next__(self):
        """
        Generates the next number in the Fibonacci sequence.
        :return: int: The next Fibonacci number in the sequence.
        :raises: StopIteration: When the specified number of terms has been generated.
        """
        if self.count > self.num:
            raise StopIteration

        if self.count == 0:
            self.count += 1
            return 0  # Return first fibonacci number
        if self.count == 1:
            self.count += 1
            return 1  # Return second fibonacci number
