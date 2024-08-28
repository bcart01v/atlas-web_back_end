#!/usr/bin/env python3
from typing import Callable
"""
This module takes a mixded list of floats and ints and
returns the sum of the floats.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the
          result of multiplying it by the multiplier.
    """

    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
