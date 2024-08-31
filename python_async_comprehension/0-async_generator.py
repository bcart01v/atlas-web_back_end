#!/usr/bin/env python3
"""

"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously generates 10 random numbers.
    
    It loops 10 times, each time waiting for 1 second, 
    and then yields a random float between 0 and 10.
    
    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding random floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
