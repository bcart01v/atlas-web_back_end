#!/usr/bin/env python3
"""
Module takes a list of floats and returns the sum of the floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns the sum of the floats

    Args:
        input_list (List[float]): a list of floats that will be summed.

     Returns:
        input_list: the sum of the floats in the list.
    """
    return sum(input_list)
