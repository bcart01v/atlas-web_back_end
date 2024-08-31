#!/usr/bin/env python3
"""
This module takes a mixded list of floats and ints and
returns the sum of the floats.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function returns a tuple with the key and the value squared.

    Args:
        K (str): a string that will be the key.
        V (Union[int, float]): a number that will be squared.

     Returns:
        Tuple[str, float]: a tuple with the key and the value squared.
    """
    return (k, float(v**2))
