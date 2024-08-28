#!/usr/bin/env python3
from typing import List, Union
"""
This module takes a mixded list of floats and ints and
returns the sum of the floats.
"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    This function returns the sum of the floats in a mixed list.

    Args:
        mxd_list (List[Union[int, float]]): a list of floats and ints.

     Returns:
        float: the sum of all the numbers in the list.
    """
    return sum(mxd_list)
