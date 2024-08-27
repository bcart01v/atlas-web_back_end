#!/usr/bin/env python3
import math
"""
This module takes a float and returns the floor of the float.
It uses Python's math module to calculate the floor of the float.
"""


def floor(n: float) -> int:
    """
    This function takes a float and returns the floor of the float.

    Args:
        n (float): a float argument that will be calculated.

     Returns:
        int: The Floor of the float.
    """
    newval = math.floor(n)
    return newval
