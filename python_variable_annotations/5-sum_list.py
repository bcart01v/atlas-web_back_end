#!/usr/bin/env python3
from typing import List
"""
This module takes a list of floats and returns the sum of the floats.
"""


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns the sum of the floats

    Args:
        input_list (List[float]): a list of floats that will be summed.

     Returns:
        input_list: the sum of the floats in the list.
    """
    return sum(input_list)
