#!/usr/bin/env python3
"""This module defines the method task_wait_n"""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """This method runs 2 process at the same time"""

    num_list: list = []
    inserted = False
    for i in range(n):
        rand = await task_wait_random(max_delay)
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
