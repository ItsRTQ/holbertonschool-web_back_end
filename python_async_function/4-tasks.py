#!/usr/bin/env python3
"""This module defines task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create a list of n elements using async with task_wait_random"""

    rand_list = []
    tasks = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        rand_list.append(await task)

    return sorted(rand_list)
