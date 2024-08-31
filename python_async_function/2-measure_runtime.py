#!/usr/bin/env python3
import time
import asyncio
import importlib


module_name = "0-main"
module = importlib.import_module(module_name)

wait_n = getattr(module, "wait_n")

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        float: The average time per call.
    """

    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time

    return total_time / n