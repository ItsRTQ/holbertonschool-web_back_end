#!/usr/bin/env python3
"""This module defines wait_n"""
import asyncio
from typing import List

task_wait_n = __import__('4-tasks').task_wait_n


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This method creates a list of n elements using async"""

    rand_list = []
    temp = []

    for i in range(n):
        temp.append(asyncio.create_task(task_wait_n(max_delay)))
    for number in asyncio.as_completed(temp):
        rand_list.append(await number)

    return sorted(rand_list)
