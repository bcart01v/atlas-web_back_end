#!/usr/bin/env python3
"""
Module for basic async syntax, takes in an integer argument and returns a float.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """
    Waits for a random delay between 0 and max_delay seconds (inclusive)
    and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The random delay value.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
