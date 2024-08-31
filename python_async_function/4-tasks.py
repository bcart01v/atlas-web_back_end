#!/usr/bin/env python3
"""
Module that calls the wait_random coroutine n times
with the specified max_delay.
"""
import asyncio
from typing import List


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        asyncio.Task: A Task object for the wait_random coroutine.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a list of all delays.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
