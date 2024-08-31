#!/usr/bin/env python3
import importlib
import asyncio

module_name = "0-basic_async_syntax"
module = importlib.import_module(module_name)

wait_random = getattr(module, "wait_random")


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        list[float]: A list of delays in ascending order.
    """

    tasks = [await wait_random(max_delay) for _ in range(n)]
    return sorted(tasks)
