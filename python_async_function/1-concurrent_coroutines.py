#!/usr/bin/env python3
"""This module defines wait_n"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """This method creates a list of n elements using async"""

    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    queue = asyncio.Queue()
    for result in results:
        await queue.put(result)
    while not queue.empty():
        delays.append(await queue.get())
    return delays
