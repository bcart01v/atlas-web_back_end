#!/usr/bin/env python3
"""
Module containing a function that genrates 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using
    an async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers
        collected from async_generator.
    """
    return [number async for number in async_generator()]
