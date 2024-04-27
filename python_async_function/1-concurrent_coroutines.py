#!/usr/bin/env python3
"""This module defines wait_n"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """This method creates a list of n elements using async"""

    num_list = []

    async def insert_sorted_list(rand):
        """Helper for parent method"""
        nonlocal num_list
        if not num_list:
            num_list.append(rand)
        else:
            inserted = False
            for indx, j in enumerate(num_list):
                if rand < j:
                    num_list.insert(indx, rand)
                    inserted = True
                    break
            if not inserted:
                num_list.append(rand)

    tasks = [insert_sorted_list(await asyncio.create_task(wait_random(max_delay))) for _ in range(n)]
    await asyncio.gather(*tasks)
    
    return num_list
