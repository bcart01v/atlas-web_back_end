#!/usr/bin/env python3
import time
import asyncio
import importlib
module_name = "1-concurrent_coroutines"
module = importlib.import_module(module_name)
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        float: The average time per call.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    total_time = stop_time - start_time

    return total_time / n