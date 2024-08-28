#!/usr/bin/env python3
from typing import List, Tuple
"""
This module takes a mixded list of floats and ints and
returns the sum of the floats.
"""


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings and returns a list of tuples,
    where each tuple contains a string and its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, each containing
        a string and its length.
    """
    return [(i, len(i)) for i in lst]
