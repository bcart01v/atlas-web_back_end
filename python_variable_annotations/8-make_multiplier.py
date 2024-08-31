#!/usr/bin/env python3
"""
This module takes a mixded list of floats and ints and
returns the sum of the floats.
"""
from typing import Callable


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
