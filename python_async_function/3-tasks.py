#!/usr/bin/env python3
"""
Module that contains a function that takes an integer and returns a 
Task object.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        asyncio.Task: A Task object for the wait_random coroutine.
    """

    return asyncio.create_task(wait_random(max_delay))
