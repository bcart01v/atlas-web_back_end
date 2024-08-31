#!/usr/bin/env python3
"""
Module containing a function that genrates 10 random numbers.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
        float: The total runtime for executing async_comprehension four times in parallel.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
