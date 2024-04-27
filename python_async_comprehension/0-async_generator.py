#!/usr/bin/env python3
"""This module defines async_generator method"""
import asyncio
import random


async def async_generator():
    """This method generates random numbers from 0 - 10"""
    rand_list = []
    for i in range(10):
        random_num = random.randint(0, 10)
        await asyncio.sleep(1)
        yield rand_list.append(random_num)
    return rand_list
