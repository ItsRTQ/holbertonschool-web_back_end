#!/usr/bin/env python3
"""This module defines wait_n"""
import asyncio
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """This method creates a list of n elements using async"""

    delays = []

    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        delay = await task
        heapq.heappush(delays, delay)
    sorted_delays = []
    while delays:
        sorted_delays.append(heapq.heappop(delays))
    return sorted_delays
