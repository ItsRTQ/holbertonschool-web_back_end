#!/usr/bin/env python3
"""This module defines wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This method creates a list of n elements using async"""

    num_list: list = []
    inserted = False
    for i in range(n):
        rand: float = await wait_random(max_delay)
        inserted = False
        if not num_list:
            num_list.append(rand)
        else:
            for indx, j in enumerate(num_list):
                if rand < j:
                    num_list.insert(indx, rand)
                    inserted = True
                    break
            if not inserted:
                num_list.append(rand)
    return num_list
