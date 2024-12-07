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
        This method returns the value of the Fibonacci number for the current iteration,
        stored in `previous_fib`, and then updates the internal state for the next iteration.
        The `current_num` is updated to the value of `next_num`, and `next_num` is updated
        to the sum of the previous two Fibonacci numbers.

        :return: int: The Fibonacci number for the current iteration (stored in 'previous_fib').
        :raises: StopIteration: When the specified number of terms has been generated.
        """
        if self.count >= self.num + 1:
            raise StopIteration

        self.count += 1
        previous_fib = self.current_num
        self.current_num = self.next_num
        self.next_num = self.current_num + previous_fib
        return previous_fib
