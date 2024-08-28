#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence
"""
This module takes a mixded list of floats and ints and
returns the sum of the floats.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., strings,
        lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
