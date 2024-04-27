#!/usr/bin/env python3
"""This module defines wait_n"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """This method creates a list of n elements using async"""

    rand_list = []
    temp = []

    for i in range(n):
        temp.append(wait_random(max_delay))

    for number in asyncio.as_completed(temp):
        rand_list.append(await number)
    return sorted(rand_list)
