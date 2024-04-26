#!/usr/bin/env python3
"""This module defines a async function name wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """This method waits for rand_num then returns it"""

    rand_num = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(rand_num)
    return rand_num
